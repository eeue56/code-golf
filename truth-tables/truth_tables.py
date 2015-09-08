def y(f, b):
    t=lambda x:bin(x)[2:][::-1]
    return'\n'.join(','.join(map(str,a+[f(*a)]))for a in[[l>'0'for l in t(x)]+[3<1]*(b-len(t(x)))for x in range(2**b)])
