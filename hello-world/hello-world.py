l = True
t = l + l 
f = t + l 
e = t * t * t + t 
h = e * e
m = h + t * t * t
o = e * (e + l) + l
a = [e * (t + f + t) + t,
    h + l,
    m, 
    m, 
    o, 
    e * t * t + t + t, 
    e * f + t, 
    h + e + f * f, 
    o, 
    h + e+ t + t, 
    m, 
    h, 
    e * f + f 
 ]
print reduce(lambda x,y : x+y, map(chr, a))
