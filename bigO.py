# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# example of algorithm that is 0(n) (time to run is linear, or proportional to size)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)



# runs n + n = 2n = O(2n) = O(n) -- when writing equation for algorithm, drop constants
def print_items(n):
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j)

print_items(10)


# ~100 items -- n*n = n^2 = O(N^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)

# ~1000 items -- n*n*n = n^3 = O(N^2) -- still exponential growth, 
# so we simplify by dropping 3 and keeping 2
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

print_items(10)







# O(n^2 + n) = O(n^2) as we drop non-dominants; the latter 'n' is inconsequential
def print_items(n):
    # n^2
    for i in range(n):
        for j in range(n):
            print(i,j)
        
        # latter 'n'
        for k in range(n):
            print(i, j, k)

print_items(10)

# O(2) = O(1): number of operations remains constant regardless of value of n
def add_items(n):
    return n + n + n


# O(N) + O(N) != O(2N) != O(N)
# O(N) + O(N) == O(a + b)
def print_items(a, b):
    for i in range(a):
        print(i)
        
    for j in range(b):
        print(j)

print_items(10)








































