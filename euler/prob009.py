from math import sqrt

"""  """
def triplet(n):
    for i in range(1,n,1):
        for j in range(1,n,1):
            k = n-i-j
            if i**2+j**2==k**2:
                l=[i, j, k, i*j*k]
                return l
    return 0

print triplet(1000)
