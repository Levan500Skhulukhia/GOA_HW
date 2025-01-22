def valid_phone_number(phone_number):
    
    if len(phone_number) != 14:
        return False

    if phone_number[0] != '(' or phone_number[4] != ')' or phone_number[5] != ' ' or phone_number[9] != '-':
        return False

    if not (phone_number[1:4].isdigit() and phone_number[6:9].isdigit() and phone_number[10:].isdigit()):
        return False

    return True





def clean_string(s):
    stack = []
    for char in s:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)



def highest_rank(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_frequency = 0
    result = None
    for num in frequency:
        if frequency[num] > max_frequency or (frequency[num] == max_frequency and num > result):
            max_frequency = frequency[num]
            result = num
            
    return result    