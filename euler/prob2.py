fibonacci=[0,1,1]
while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

fibonacci.remove(fibonacci[-1])

j=0
for i in fibonacci:
    if i%2==0:
        j+=i

print j
