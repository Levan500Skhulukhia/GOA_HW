def merge_strings(first, second):
    for i in range(len(first), 0, -1):
        if first[-i:] == second[:i]:
            return first + second[i:]
    return first + second



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



def gimme_the_letters(sp):
    start, end = sp.split('-')
    return ''.join(chr(i) for i in range(ord(start), ord(end) + 1))



def number(bus_stops):
    
    total_people = 0
    
    # Iterate through each bus stop's data
    for on, off in bus_stops:
        total_people += on  # Add the number of people getting on the bus
        total_people -= off  # Subtract the number of people getting off the bus
    
    # Return the final number of people on the bus
    return total_people




def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])





def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i + 1]) != ord(chars[i]) + 1:
            return chr(ord(chars[i]) + 1)
