from sympy import sympify

def calculate_expression(expression):
    try:
        expr = sympify(expression)
        return float(expr)
    except Exception as e:
        return str(e)

expression = "(2+3) * 2 *100"
result = calculate_expression(expression)
print(result)