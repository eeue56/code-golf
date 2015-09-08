def f(*s):
    def b(*a):
        for x, y in zip(s[:-1], a):
            locals()[x] = y
        return eval(s[-1][::-1].replace("$", "", 1)[::-1])
    return b
