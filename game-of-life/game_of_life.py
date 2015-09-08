z = len
u = x = y = r = 0
def v():
    global u
    if z(r) < 3:
        if y < 1:
            c, n = r
        else:
            n, c = r
        s = 0
    else:
        l, c, n = r
        s = l[x - 1] + l[x] + (l[x+1] if x == z(l) else 0)

    u = s + {x : sum(c[x - 1:x+2] + n[x - 1:x + 2]) - c[x],
        0 : n[0] + n[1] + c[1],
        z(c) - 1 : n[x - 1] + n[x] + c[x - 1]
        }[x]


def d(w):
    global r, x, y
    a = list.append
    m = [[int(i) for i in l.strip()] for l in open(w)]

    n = range(1, z(m))
    
    r = m[0:2]
    v() 
    e = [{u:0,2: r[0][0], 3: 1}[u]]

    for x in n:
        v()
        a(e, {u:0,2: r[1][x], 3: 1}[u])
    o = [e]

    for y in n:
        r = m[y - 1:y + 2]
        x = 0
        v()  
        e = [{u:0,2: r[1][1], 3: 1}[u]]

        for x in n:
            v()
            a(e, {u:0,2: r[1][x], 3: 1}[u])
        a(o, e)

    f = open(w, 'w')
    f.write('\n'.join(''.join(map(str, q)) for q in o))
