def w(k):
    o = ''
    while k:
        m = lambda x : k/x == (k + 0.0)/x
        l = 'Fizz'
        b = 'Buzz'
        o = [`k`, [b, l][m(3)], l+b][m(3) + m(5)] + '\n' + o
        k -= 1
    return o
