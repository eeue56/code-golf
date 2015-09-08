# Challenge

Define a function that prints a truth table. It should take 2 arguments. The first should be a function that takes in x arguments and returns True or False. The second should be x, the number of arguments for the function.
Output should be along the lines of
```
1, 2, O
False, False, False
False, True, False
True, False, False
True, True, True
```
where O is (\x y -> x && y)
