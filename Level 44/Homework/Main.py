def dup(arry):
    
    result = []
    for s in arry:
        processed = []
        
        # Iterate through  character in the string
        for char in s:
            # Only add the character if its not the same as the last one added
            if not processed or processed[-1] != char:
                processed.append(char)
        
        # Join the list of characters into string and add it to the result list
        result.append(''.join(processed))
    
    return result


def encode(st):
    result = ""
    
    for char in st:
        # Check if the character is  vowel and replace it with  corresponding number
        if char == 'a':
            result += '1'
        elif char == 'e':
            result += '2'
        elif char == 'i':
            result += '3'
        elif char == 'o':
            result += '4'
        elif char == 'u':
            result += '5'
        else:
            # If its not vowel, just add the character as it is
            result += char
    
    return result

def decode(st):
    
    result = ""
    
    
    for char in st:
        # Check if the character is a number and replace it with the corresponding vowel
        if char == '1':
            result += 'a'
        elif char == '2':
            result += 'e'
        elif char == '3':
            result += 'i'
        elif char == '4':
            result += 'o'
        elif char == '5':
            result += 'u'
        else:
            # If its not  number, just add the character as it is
            result += char
    
    
    return result

