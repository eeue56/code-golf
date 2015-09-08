f [x] [y] = [x, y]
f (x:t) (y:p) = x : y : f t p
zipper = f
