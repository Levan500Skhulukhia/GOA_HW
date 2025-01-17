def number_to_string(num):
    return str(num)



def make_negative( number ):
    num = number + number
    
    if number > 0:
        return number - num
    else: 
        return number
    
    
    
def generate_shape(n):
   
    return "\n".join(["+" * n] * n)




def opposite(number):
    num = number + number
    
    if number < 0:
        return number - num
    elif number > 0:
        return number - num
    else: 
        return number
    
    
    
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
    
    
def remove_char(s):
    
     return s[1:-1]
 
 
 
 
def count_sheeps(sheep):
    sum = 0
    
    for i in sheep:
        if i == True:
            sum += 1
        
    return sum




def no_space(x):
    result = x.replace(" ", "")
    return result




def basic_op(operator, value1, value2):
    result = 0
    if operator == "+":
        result = value1 + value2
    elif operator == "-":
        result = value1 - value2
    elif operator == "*":
        result = value1 * value2
    elif operator == "/":
        result = value1 / value2
        
    return result




def paperwork(n, m):
    if n <= 0 or m <=0:
        return 0
    else:
        return n * m