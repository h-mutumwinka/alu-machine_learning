#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

bottom = np.zeros(fruit.shape[1])

for i in range(fruit.shape[0]):
    plt.bar(people, fruit[i], bottom=bottom, color=colors[i], width=0.5, label=fruits[i])
    bottom += fruit[i] 

plt.ylabel("Quantity of Fruit")
plt.yticks(np.arange(0, 81, 10))
plt.title("Number of Fruit per Person")
plt.legend()
plt.show()

