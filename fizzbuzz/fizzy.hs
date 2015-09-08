import Data.Char

u = concat

q x 
    | x < w = [j e]
    | h $ r $ f * p = u [l, s, n] : d
    | h $ r p = c l 
    | h $ r f = c n 
    | w > o = c e  
        where
            o = length [[]]
            w = o + o
            p = w + o
            f = w + p
            t = f * w
            z = t * (t + w) + w
            s = m [t * p + w]
            l = m [t * (f + w), t * t + f, z, z]
            n = m [t * (f + o) + f + o, t * t + t + f + w, z, z]
            j x = u [x, m [(w + w) * t + w + w], s]
            m = map chr
            d = q $ x - o
            r = rem x
            e = show x
            c x = j x : d
            h x = x == o - o
            
f = putStr . u . reverse . q

main = f 15 
