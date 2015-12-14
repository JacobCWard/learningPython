# This is my own solution to the problem.
# ~10s to run

import functools
import time

stTime=time.time()

def triangular(n):
    return sum(range(n+1))

def factorize(n):
    return list(set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

factors = []
triX = 0

while len(factors)<=500:
    triX+=1
    factors = factorize(triangular(triX))

endTime=time.time()
t1=endTime-stTime

print(t1)
print(len(factors))
print(triangular(triX))
