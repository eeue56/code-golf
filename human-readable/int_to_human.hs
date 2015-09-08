f x=let b=div((length$show x)-2)3in show(x/1024^b)++(" KMGT"!!b):"B"
