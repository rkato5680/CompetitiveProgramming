def ternary_search(f, x_min, x_max, epsilon=1e-15):
    while True:
        x1,x2 = 1/3*(x_max-x_min)+x_min,2/3*(x_max-x_min)+x_min
        gap = f(x1)-f(x2)
        if gap < 0: x_max=x2
        else: x_min=x1
        if abs(gap) <= epsilon:break
    return (x_max+x_min)/2



# multi-dimensional ternary search

def norm(x):
    x = np.array(x)
    return np.sqrt((x**2).sum())

def ternary_searchND(f, x_min, x_max, eps=1e-12, dim=2):
    x_min, x_max = map(lambda x: np.array(x, dtype=float), [x_min, x_max])
    while True:
        for i in range(dim):
            x1, x2 = (x_max + x_min)/2, (x_max + x_min)/2
            x1[i], x2[i] = 1/3*(x_max[i]-x_min[i])+x_min[i],2/3*(x_max[i]-x_min[i])+x_min[i]
            if f(*x1) < f(*x2): x_max[i] = x2[i]
            else: x_min[i] = x1[i]
        if norm(x_max[i] - x_min[i]) <= eps:break
    return (x_max + x_min) / 2
