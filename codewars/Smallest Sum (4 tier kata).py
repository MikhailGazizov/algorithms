"""
Description
Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:

if X[i] > X[j] then X[i] = X[i] - X[j]

When no more transformations are possible, return its sum ("smallest possible sum").
"""

# My theory is that I shouldn't always try and count the sum one by one, but rather find formula.
# Biggest common denominator times the lenght of the input array might be the answer
from test_utils import test_it

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def solution(lst):
    if len(lst) <= 1: return lst[0]
    for i in range(1,len(lst)):
        lst[i] = GCD(lst[i], lst[i - 1])
    return lst[-1]*len(lst)


input_data = [
    [9],
    [6,9,21],
    [1,21,55]
]
solutions = [
    9,
    9,
    3
]

test_it(solution, input_data, solutions)