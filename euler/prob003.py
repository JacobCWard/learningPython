number=600851475143
factors=[]
i=2
while i<number:
    while number%i!=0:
        i+=1
    factors.append(i)
    number/=i
    i+=1
print factors
