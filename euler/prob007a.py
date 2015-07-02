primes=[]

def is_prime(x):
    n=x-1
    if x<2:
        return False
    while n>1:
        if x%n==0:
            return False
        n-=1
    return True

i=0

while len(primes)<=100000:
    if is_prime(i):
        primes.append(i)
        print len(primes), i
    i+=1

print primes[-1]
