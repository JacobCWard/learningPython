def divisible_under_20():
    reached=lowest=20
    i=380
    while reached > 0:
        if i%reached==0:
            reached-=1
            if reached < lowest:
                lowest=reached
            print reached, i, lowest
        else:
            reached=20
            i+=380
    return i

divisible_under_20()
