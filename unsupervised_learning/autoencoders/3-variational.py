#!/usr/bin/env python3
"""
Defines function that creates a variational autoencoder
"""


import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    Creates a variational autoencoder
    """
    if type(input_dims) is not int:
        raise TypeError(
            "input_dims must be an int containing dimensions of model input")
    if type(hidden_layers) is not list:
        raise TypeError("hidden_layers must be a list of ints \
        representing number of nodes for each layer")
    for nodes in hidden_layers:
        if type(nodes) is not int:
            raise TypeError("hidden_layers must be a list of ints \
            representing number of nodes for each layer")
    if type(latent_dims) is not int:
        raise TypeError("latent_dims must be an int containing dimensions \
        of latent space representation")

    # Sampling layer for VAE
    def sampling(args):
        """Reparameterization trick by sampling from isotropic unit Gaussian.
        # Arguments
            args (tensor): mean and log of variance of Q(z|X)
        # Returns
            z (tensor): sampled latent vector
        """
        z_mean, z_log_var = args
        batch = keras.backend.shape(z_mean)[0]
        dim = keras.backend.shape(z_mean)[1]
        epsilon = keras.backend.random_normal(shape=(batch, dim))
        return z_mean + keras.backend.exp(0.5 * z_log_var) * epsilon

    # encoder
    encoder_inputs = keras.Input(shape=(input_dims,))
    encoder_value = encoder_inputs

    # Hidden layers
    for i in range(len(hidden_layers)):
        encoder_layer = keras.layers.Dense(hidden_layers[i],
                                           activation='relu')
        encoder_value = encoder_layer(encoder_value)

    # Latent space - mean and log variance
    z_mean = keras.layers.Dense(latent_dims,
                                name='z_mean')(encoder_value)
    z_log_var = keras.layers.Dense(latent_dims,
                                   name='z_log_var')(encoder_value)

    # Sample from latent space
    z = keras.layers.Lambda(sampling, output_shape=(latent_dims,),
                            name='z')([z_mean, z_log_var])

    encoder = keras.Model(inputs=encoder_inputs,
                          outputs=[z_mean, z_log_var, z])

    # decoder
    decoder_inputs = keras.Input(shape=(latent_dims,))
    decoder_value = decoder_inputs

    # Reverse the hidden layers
    for i in range(len(hidden_layers) - 1, -1, -1):
        decoder_layer = keras.layers.Dense(units=hidden_layers[i],
                                           activation='relu')
        decoder_value = decoder_layer(decoder_value)

    decoder_output_layer = keras.layers.Dense(units=input_dims,
                                              activation='sigmoid')
    decoder_outputs = decoder_output_layer(decoder_value)
    decoder = keras.Model(inputs=decoder_inputs, outputs=decoder_outputs)

    # autoencoder (VAE)
    inputs = encoder_inputs
    z_mean_out, z_log_var_out, z_out = encoder(inputs)
    outputs = decoder(z_out)
    auto = keras.Model(inputs=inputs, outputs=outputs)

    # VAE loss
    def vae_loss(x_true, x_decoded):
        reconstruction_loss = keras.losses.binary_crossentropy(x_true,
                                                               x_decoded)
        reconstruction_loss *= input_dims
        kl_loss = 1 + z_log_var_out - keras.backend.square(z_mean_out) - \
            keras.backend.exp(z_log_var_out)
        kl_loss = keras.backend.sum(kl_loss, axis=-1)
        kl_loss *= -0.5
        return keras.backend.mean(reconstruction_loss + kl_loss)

    auto.compile(optimizer='adam', loss=vae_loss)

    return encoder, decoder, auto
