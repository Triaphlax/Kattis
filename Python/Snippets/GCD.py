def gcd(a, b):

    while not a == 0:
        if a == 0:
            break
        else:
            temp = a
            a = b%a
            b = temp
     
    return b