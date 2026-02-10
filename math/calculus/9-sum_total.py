#!/usr/bin/env python3
'''
    a function def summation_i_squared(n):
    that calculates the summation
    of all numbers from 1 to n
'''


def summation_i_squared(n):
    '''
    calculates the summation
    of all numbers from 1 to n
    '''
    if type(n) is not int or n < 1:
        return None
    sigma_sum = (n * (n + 1) * ((2 * n) + 1)) / 6
    return int(sigma_sum)
