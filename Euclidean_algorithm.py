def MDC(a, b):
    if b > a:
        a, b = b, a
    if a == b:
        return a
    if b == 0:
        return a

    i = a
    j = b  
    while j != 0:
        q = i // j
        r = i % j 
        i = (q * j) + r

        i = j
        j = r
        
    return i
        
