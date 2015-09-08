def f(n):
    
    g = int(n / 2.5)


    o = []
    p = o.append
    z = []
    j = z.append

    y = n
    while 1:
        y /= 2
        if y == n % 2:
            j(2)
        if y < 2:
            break
        j(y)


    x = g
    while 1:
        x /= 2
        if n % 2:
            if x < 2:
                p(2)
                break
            if x % 2:
                p(x + 1)
        else:
            if x < 2:
                break
            p(x)


    i = 2
    s = 1
    l = '+' + '-' * n + '+\n'

    while s <= g:
        b = '|'
        a = 2**i

        x = 1
        while x <= n:
            b += ('|' if s < x else '-' if s==x or s in o else ' ') if x in z else ('-' if (i > 2 == x + 1 <= a) or x <= a else ' ') if s in o else ' '
            x += 1
        if '-' in b:
            i += 1
        
        s += 1
        l +=  b + '|\n'

    print l + '+' + '-' * n + '+'
