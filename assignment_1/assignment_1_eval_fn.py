def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

expression = "(2+3*11)+5*20"
result = calculate_expression(expression)
print(result)
