def f(x, y):
    l = []
    t = 0

    while t < len(x):
        l += [x[t], y[t]]
        t += 1
    return l

c = chr

locals()[c(122) + c(105) + 2 * c(112) + c(101) + c(114)] = f
