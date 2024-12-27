def calculate(s):
    
    string1 = " ".join(s.replace("plus", "+").replace("minus", "-").split("+"))
    str2 = string1[0]
    for i in string1[1:]:
        if i == "-":
            str2 += " -"
        else:
            str2 += i
    
    result = 0
    
    for i in str2.split():
        result += int(i)
    return str(result)




def even_or_odd(s):
    even = 0
    odd = 0
    
    for i in s:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
            
    if even > odd: return "Even is greater than Odd"
    elif even < odd: return "Odd is greater than Even"
    else: return "Even and Odd are the same"





def nth_char(words):
    result = ""
    index = 0
    for i in words:
        result += i[index]
        index += 1
    return result





def freq_seq(s, sep):
  
    counts = []
    
    
    for char in s:
        count = s.count(char)  
        counts.append(str(count))  
    
   
    result = sep.join(counts)
    return result






def reverse_it(data):
    if type(data) == str:
        reversed_string = ""
        for char in data:
            reversed_string = char + reversed_string
        return reversed_string
    elif type(data) == int or type(data) == float:
        reversed_number = ""
        for char in str(data):
            reversed_number = char + reversed_number
        if "." in reversed_number:
            return float(reversed_number)
        else:
            return int(reversed_number)
    else:
        return data



if not arr:
        return []
    
    missing = []  # This should be outside the if block
    
    for num in range(arr[0], arr[-1] + 1):
        if num not in arr:
            missing.append(num)
    
    return missing




def only_duplicates(st):
    result = ""
    for char in st:
        if st.count(char) > 1:
            result += char
    return result