from math import floor

def median(intList):
    print intList
    intList=sorted(intList)
    print intList
    index=int(floor(len(intList)/2))
    print index
    print intList[index]
    print intList[index-1]
    print (intList[index]+intList[index-1])//2
    if len(intList)%2==0:
        return (intList[index]+intList[index-1])//2
    else:
        return intList[index]

print median([4,5,5,4])
