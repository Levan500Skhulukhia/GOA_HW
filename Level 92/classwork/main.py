def elevator_distance(array):
    total_distance = 0
    
    for i in range(1, len(array )):
        if array[i] > array[i - 1]:
            total_distance += array[i] - array[i - 1]
        else:
            total_distance += array[i - 1]- array[i]
    
    return total_distance





def count_letters_and_digits(s):
    count = 0
    
    for char in s:
        is_letter = False
        is_digit = False
        
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            if char == letter:
                is_letter = True
                break
        
        if not is_letter:
            for digit in "0123456789":
                if char == digit:
                    is_digit = True
                    break
        
        if is_letter or is_digit:
            count += 1
    
    return count






def longest_collatz(arr):
    def collatz_length(n):
        length = 1
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            length += 1
        return length
    
    max_length = 0
    result = arr[0]
    
    for num in arr:
        current_length = collatz_length(num)
        if current_length > max_length:
            max_length = current_length
            result = num
    
    return result

def multiplication_table(size):
    table = []
    
    for i in range(size):
        row = []
        
        for j in range(size):
            product = (i + 1) * (j + 1)
            row.append(product)
        
        table.append(row)
    
    return table #goodluck

