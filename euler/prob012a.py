# This is the first suggested solution from the Project Euler pdf for this problem.
# Unable to run in a reasonable time

import time

stTime=time.time()

t = 1
a = 1
cnt = 0
while cnt <= 500:
    cnt = 0
    a+=1
    t+=a
    for i in range(1,t+1):
        if t%i==0:
            cnt+=1

endTime=time.time()
t1=endTime-stTime
print(t1)

print(t)
