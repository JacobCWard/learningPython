from math import floor, sqrt
import time

sTime=time.time()

def is_prime(n):
    if n<=1:
        return False
    elif n<4:
        return True
    elif n%2==0:
        return False
    elif n<9:
        return True
    elif n%3==0:
        return False
    else:
        r=floor(sqrt(n))
        f=5.0
        while f <= r:
            if n%f==0:
                return False
            if n%(f+2)==0:
                return False
            f+=6
    return True

i=0
primes=[]
while len(primes)<=1000000:
    if is_prime(i):
        primes.append(i)
    i+=1

print primes[-1]

eTime=time.time()
print eTime-sTime
