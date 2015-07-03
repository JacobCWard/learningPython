import time

stTime=time.time()
execfile("prob007.py")
endTime=time.time()
t1=endTime-stTime

stTime=time.time()
execfile("prob007a.py")
endTime=time.time()
t2=endTime-stTime

stTime=time.time()
execfile("prob007b.py")
endTime=time.time()
t3=endTime-stTime

print t1, t2, t3
