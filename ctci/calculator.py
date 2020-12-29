def char_to_list(cs):
    temp = ""
    converted = []
    for c in cs:
        if not c.isnumeric():
            if len(temp) > 0:
                converted.append(temp)
                temp = ""
            converted.append(c)
        else:
            temp += c

    if len(temp) > 0:
        converted.append(temp)

    return converted

def find_parantheses(cs_list):
    for i, e in enumerate(cs_list):
        if e == "(":
            start = i
        elif e == ")":
            end = i
            return start, end

def parse(cs):
    left = 0
    right = 0
    operator = ""

    for c in cs:
        if c.isnumeric() and len(operator) == 0:
            left += int(c)
        elif c.isnumeric() and len(operator) > 0:
            right += int(c)
        elif not c.isnumeric() and c != "(" and c != ")":
            operator += c

    return (left, right, operator)

def calculate(parse_output):
    left = parse_output[0]
    right = parse_output[1]
    operator = parse_output[2]

    if operator == "+":
        return left + right
    elif operator == "*":
        return left * right
    elif operator == "-":
        return left - right
    elif operator == "/":
        return int(left / right)

def process_stacks(v, sv, so):
    sv.pop()
    sv.pop()
    sv.append(v)
    so.pop()

def handle_operation_precendence(output):
    # stack values
    sv = []
    # stack operations
    so = []

    for i,e in enumerate(output):
        if e.isnumeric():
            sv.append(float(e))
            if so:
                if so[-1] == "/":
                    process_stacks((sv[-2] / sv[-1]), sv, so)
                elif so[-1] == "*":
                    process_stacks(sv[-2] * sv[-1], sv, so)
        else:
            so.append(e)
    return sv, so

def calculate_linear_output(sv, so):
    res = 0
    for i in range(len(so)):
        if so[i] == "+":
            if res == 0:
                res = sv[i] + sv[i+1]
            else:
                res += sv[i+1]
        else:
            if res == 0:
                res = sv[i] - sv[i+1]
            else:
                res -= sv[i+1]

    return res if res != 0 else sv[0]

def calculator(cs):
    output = char_to_list(cs)

    while "(" in output:
        s, e = find_parantheses(output)
        parsed = parse(output[s:e])
        res = calculate(parsed)
        output[s:e+1] = str(res)
        output = char_to_list(output)
    print(output)
    sv, so = handle_operation_precendence(output)
    return calculate_linear_output(sv, so)

cs = '24+78/(6*(9+5))*2+6+(8*(3+5))'
# cs = '2+(12+10)-(3+4)'
# cs = '25/6'

print("Custom calculator output:   %s" %calculator(cs))
print("Python output:              %s" %eval(cs))