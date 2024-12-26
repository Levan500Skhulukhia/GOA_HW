def dont_give_me_five(start,end):
    numbers = range(start, end + 1)
    
    # Filter out numbers that contain the digit '5'
    filtered_numbers = [num for num in numbers if '5' not in str(num)]
    
    # Return the count of the filtered numbers
    return len(filtered_numbers)



def capitalize(s):
    even_capitalized = ''.join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(s)
    )
    
    odd_capitalized = ''.join(
        char.upper() if i % 2 != 0 else char.lower()
        for i, char in enumerate(s)
    )
    
    return [even_capitalized, odd_capitalized]




def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")  
        elif i % 3 == 0:
            result.append("Fizz")     
        elif i % 5 == 0:
            result.append("Buzz")     
        else:
            result.append(i)           
    return result




def up_array(arr):
    
    if not arr:  # Check if the array is empty
        return None
    for num in arr:  # Check for invalid elements
        if num < 0 or num > 9:
            return None

   
    number_str = ""
    for num in arr:
        number_str += str(num)  # Build the number as a string
    number = int(number_str) + 1  

    # Convert the result back to an array of digits
    result = []
    result_number_str = str(number)

    
    while len(result_number_str) < len(arr):
        result_number_str = '0' + result_number_str  # Add leading zeros if necessary

    for digit in result_number_str:
        result.append(int(digit))  # Add each digit to the result list

    return result