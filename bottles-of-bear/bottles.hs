r = reverse
c = concat
s = show
b = "reeb fo selttob"

v x = [a | a <- b, a /= 's' || x > 1]

main = putStrLn $ c $ [c [s x,
		r $ " ,llaw eht no " ++ v x ++ " ",
		s x,
		r $ " ,dnuora ti ssap dna nwod eno ekaT\n." ++ v x ++ " ",
		if x > 1 then s $ x - 1 else r "erom on",
		r $ "\n\n." ++ b ++ " "] 
		| x <- r [1..99]] ++ 
		[r $ c ["llaw eht no ", b, " 99 ,erom emos yub dna erots eht ot oG\n.", b, " erom on ,", b, " erom oN"]]
