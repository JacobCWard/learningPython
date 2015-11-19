from math import floor, sqrt

def isPrime(n):
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

limit=2000000
primeSum=5
n=5
while n<=limit:
    if isPrime(n):
        print n
        primeSum+=n
        n+=2
    if n<=limit and isPrime(n):
        primeSum+=n
        n+=4

print primeSum
