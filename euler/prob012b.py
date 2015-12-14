# This is the second suggested solution from the Project Euler pdf for this problem.
# ~35s to run

import time
from math import sqrt, floor

stTime=time.time()

t = 1
a = 1
cnt = 0
while cnt <= 500:
    cnt = 0
    a+=1
    t+=a
    ttx = floor(sqrt(t))
    for i in range(1,ttx+1):
        if t%i==0:
            cnt+=2
        if t==ttx**2:
            cnt-=1

endTime=time.time()
t1=endTime-stTime
print(t1)

print(t)
