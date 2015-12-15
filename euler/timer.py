import time
def timer(scriptname):
    stTime=time.time()
    execfile(scriptname)
    endTime=time.time()
    t1=endTime-stTime
    print(t1)
