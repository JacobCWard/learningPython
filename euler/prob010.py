def primes_less_than(n):
    primes = [2]
    def is_prime(number):
        if number<2:
            return False
        for i in primes:
            if number%i==0:
                return False
        return True
    i=0
    while primes[-1]<=n:
        if is_prime(i):
            if(i<n)
                primes.append(i)
        i+=1
    return primes

primes2=primes_less_than(2000000)

print primes2
print sum(primes2)
