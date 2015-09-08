t y = ([x | x <- y, x > "/"], r [x | x <- y, x < "0"])
b x = read x :: Float
a (d, t) | length t < 1 = q !! 0 | 1 > 0 = a ((n : (e $ e d)), e t) 
 where 
  n = show $ case t !! 0 of
   "+" -> l + p
   "/" -> l / p
   "*" -> l * p
   _ -> l - p
  l = q !! 0
  p = q !! 1
  q = map b d
  e = tail

f = a.t.words
