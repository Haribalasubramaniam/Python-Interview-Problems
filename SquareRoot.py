"""
Arithmetic Method without using Math Module 
    def square_root(n):
    return n**0.5

n = int(input("Enter a Number : "))
print(square_root(n))

"""

import math
def square_root(n):
    return math.sqrt(n)

n = float(input("Enter a Number : "))
print(square_root(n))