g l = j $ j $ [[[if x then '1' else '0'] | x <- p] ++ [['\n']] | p <- [[s (l !! j !! i) (sum [1 | y <- [j-1..j+1], x <- [i-1..i+1],
                        x /= i || y /= j,
                        y > -1,
                        y < b,
                        x > -1,
                        x < b,
                        (l !! y) !! x]) | i <- q] | j <- q]]
    where 
        s t 3 = True
        s t 2 = t
        s t _ = t < t
        b = length l
        j = concat 
        q = [0..b -1]

p ('\n':t) = p t
p (x:t) = (x > '0') : p t
p _ = []

f n = do
        d <- readFile n
        return $ writeFile n $ g $ map p $ words d
