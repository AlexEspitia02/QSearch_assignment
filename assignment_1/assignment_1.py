def calculate_expression(expression):
    def apply_operator(ops, values):
        operator = ops.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+': values.append(left + right)
        elif operator == '-': values.append(left - right)
        elif operator == '*': values.append(left * right)
        elif operator == '/': values.append(left / right)

    def precedence(op):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 0

    values = []
    ops = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = (val * 10) + int(expression[i])
                i += 1
            values.append(val)
            i -= 1
        elif expression[i] == '(':
            ops.append(expression[i])
        elif expression[i] == ')':
            while ops and ops[-1] != '(':
                apply_operator(ops, values)
            ops.pop()  # remove '('
        else:
            while (ops and precedence(ops[-1]) >= precedence(expression[i])):
                apply_operator(ops, values)
            ops.append(expression[i])
        i += 1

    while ops:
        apply_operator(ops, values)

    return values[-1]

expression = "(2+3-1) * 2 * 7"
result = calculate_expression(expression)
print(result)
