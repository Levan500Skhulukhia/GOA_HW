def derive(coefficient, exponent): 
    product = coefficient * exponent
    new_exponent = exponent - 1
    return f"{product}x^{new_exponent}"
   
   
   
   
   
   
   
def add(a, b):
    return a + b

def subt(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b






def open_or_senior(data):
    return [
        "Senior" if age >= 55 and handicap > 7 else "Open"
        for age, handicap in data ]