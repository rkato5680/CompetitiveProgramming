def polish_notation(s):
    s = s.split()
    h = deque([])
    for i in range(len(s)):
        try:
            num = int(s[i])
            h.append(num)
        except:
            num1 = h.pop()
            num2 = h.pop()
            operator = s[i]
            output = eval(str(num2) + operator + str(num1))
            h.append(output)
    return h.pop()
