threesAndFives1=range(3,1000)[::3]+range(5,1000)[::5]
threesAndFives=[]
for i in threesAndFives1:
    if i not in threesAndFives:
        threesAndFives.append(i)

print sum(threesAndFives)
