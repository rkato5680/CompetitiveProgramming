# arrayではなく整数値を検索する方式。
# funcは条件式

def binary_search2(func, n_min, n_max):
    left,right=n_min,n_max
    y_left, y_right = func(left), func(right)
    while right-left>1:
        middle = (left+right)//2
        y_middle = func(middle)
        if y_left==y_middle: left=middle
        else: right=middle

    return left
