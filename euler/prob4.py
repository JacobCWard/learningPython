factors=[range(999,99,-1),range(999,99,-1)]

def palindrome():
    palindromes=[]
    longest=0
    for i in factors[0]:
        for j in factors[1]:
            k=list(str(i*j))
            if k[0]==k[-1]:
                if k[1]==k[-2]:
                    if k[2]==k[-3]:
                        palindromes.append(int(filter(str.isdigit, repr(k))))
    for i in palindromes:
        if i>longest:
            longest=i
    return longest

print palindrome()
