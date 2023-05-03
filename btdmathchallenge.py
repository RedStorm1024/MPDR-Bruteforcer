import itertools

#0 > +
#1 > -
#2 > *
#3 > /
#4 > ^
def calc(op):
    if type(op) is int:
        return op
    a=calc(op[1])
    b=calc(op[2])
    if a is None or b is None:
        return None
    if type(a) is complex or type(b) is complex:
        return None
    if a>2**100 or b>2**100:
        return None
    if op[0] == 0:
        return a+b
    elif op[0] == 1:
        return a-b
    elif op[0] == 2:
        return a*b
    elif op[0] == 3:
        if b==0:
            return None
        return a/b
    else:
        if a==0 and b < 0:
            return None
        if b>100:
            return None
        try:
            return a**b
        except:
            return None

def generateCalc(digits, score, operands, order):
    for i in range(len(order)):
        digits[order[i]] = [operands[i], digits[order[i]], digits[order[i]+1]]
        del digits[order[i]+1]
    return digits[0]

def bruteforce(number, goal):
    okDigits = list(dict.fromkeys(list(str(number))))
    for i in range(len(okDigits)):
        okDigits[i] = int(okDigits[i])
    if 0 in okDigits:
        okDigits.remove(0)
    for digits in itertools.product(okDigits, repeat=goal):
        for operands in itertools.product(range(5), repeat=goal-1):
            operands = list(operands)
            for order in itertools.permutations(range(goal-1)):
                order = list(order)
                Ld = list(digits)
                for i in reversed(range(len(order))):
                    n = sum(1 for x in order[:i] if x < order[i])
                    order[i] -= n
                op = generateCalc(Ld, goal, operands, order)
                result = calc(op)
                if(result==number):
                    return op

def read(op):
    if type(op) is int:
        return str(op)
    a=read(op[1])
    b=read(op[2])
    if op[0] == 0:
        return "(" + a + "+" + b + ")"
    elif op[0] == 1:
        return "(" + a + "-" + b + ")"
    elif op[0] == 2:
        return "(" + a + "*" + b + ")"
    elif op[0] == 3:
        return "(" + a + "/" + b + ")"
    else:
        return "(" + a + "^" + b + ")"
