def calculator(expression : str):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid Exception"
