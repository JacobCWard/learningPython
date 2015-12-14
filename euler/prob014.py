# When checking all terms even and odd: ~73s
# Checking only odd terms: ~38s
# Checking odd terms >500001: ~20s
# Using int instead of list: ~17s

import time

stTime=time.time()
maxLen = 0

for i in range(999999,500001,-2):
    n = i
    nLen = 1
    while n > 1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        nLen+=1
    if nLen>maxLen:
        maxLen = nLen
        print(nLen,i)

endTime=time.time()
t1=endTime-stTime
print(t1)
