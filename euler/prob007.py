primes = [2]

def is_prime(number):
    if number<2:
        return False
    for i in primes:
        if number%i==0:
            return False
    return True

i=0

while len(primes)<=10000:
    if is_prime(i):
        primes.append(i)
    i+=1

print primes[-1]
