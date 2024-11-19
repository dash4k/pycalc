def postfix(s: str) -> str:
    operand = {
        '+': 1, 
        '-': 1, 
        '/': 2, 
        'x': 2,
    }

    temp = []
    pfix = []
    i = 0
    l = len(s)

    while i < l:
        c = s[i] 
        if c in operand:
            if not temp:
                temp.append(c)
            else:
                while temp and operand[c] <= operand[temp[-1]]:
                    pfix.append(temp.pop())
                temp.append(c)
        else:
            num = c
            while i + 1 < l and s[i+1] not in operand:
                i+=1
                num += s[i]
            pfix.append(num)
        i += 1
    while temp:
        pfix.append(temp.pop())
    return ' '.join(pfix)


def operation(a: str, b: str, op: str) -> str:
    a, b = float(a), float(b)
    if op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
    elif op == 'x':
        return str(a * b)
    elif op == '/':
        return str(a / b)


def calculate(s: str) -> str:
    operand = {'+', '-', '/', 'x'}
    temp = []
    i = 0
    l = len(s)

    while i < l:
        if s[i] == ' ':
            i+=1
            continue
        c = s[i]
        if c in operand:
            b = temp.pop()
            a = temp.pop()
            temp.append(operation(a, b, c))
        else:
            num = c
            while i + 1 < l and s[i+1] not in operand and s[i+1] != ' ':
                i+=1
                num += s[i]
            temp.append(num)
        i += 1
    return temp[-1]