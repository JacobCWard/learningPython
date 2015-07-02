def find_sum_of_square():
    x=0
    for i in range(1,101):
        x+=i**2
    return x

square_of_sum=sum(range(1,101))**2
sum_of_square=find_sum_of_square()

print (square_of_sum - sum_of_square)
