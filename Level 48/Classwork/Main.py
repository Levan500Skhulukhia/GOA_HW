def in_asc_order(arr):
    sorted_list = arr.copy()
    sorted_list.sort()
    
    for i in range(len(arr)):
        if sorted_list[i] != arr[i]:
            return False
    
    return True



def valid_braces(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    
    return s == ""




def expanded_form(num):
    num_str = str(num)
    result = []
    
    for i in range(len(num_str)):
        digit = num_str[i]
        
        if digit != '0':
            expanded_number = digit + '0' * (len(num_str) - i - 1)
            result.append(expanded_number)
    
    return ' + '.join(result)



def expanded_form(num):
    # Convert the number to a string so we can easily separate it
    num_str = str(num)
    
    # Split the number into integer and fractional parts
    if '.' in num_str:
        integer_part, fractional_part = num_str.split('.')
    else:
        integer_part, fractional_part = num_str, ''
    
    # List to hold the expanded parts
    result = []
    
    # Add expanded form for the integer part
    for i in range(len(integer_part)):
        digit = integer_part[i]
        # Only add if the digit is not '0'
        if digit != '0':
            # The place value is based on the position of the digit
            result.append(digit + '0' * (len(integer_part) - i - 1))
    
    # Add expanded form for the fractional part
    for i in range(len(fractional_part)):
        digit = fractional_part[i]
        # Only add if the digit is not '0'
        if digit != '0':
            result.append(f"{digit}/{10**(i + 1)}")
    
    # Join all the parts with ' + '
    return ' + '.join(result)
