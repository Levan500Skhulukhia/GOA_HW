def most_frequent_item_count(array):
    if not array:  # Check if the array is empty
        return 0
    return max(array.count(item) for item in set(array))

def move_ten(st):
    result = []
    
    for char in st:
        if char.islower():
            # Shift lowercase letter
            shifted = chr((ord(char) - ord('a') + 10) % 26 + ord('a'))
            result.append(shifted)
        elif char.isupper():
            # Shift uppercase letter
            shifted = chr((ord(char) - ord('A') + 10) % 26 + ord('A'))
            result.append(shifted)
        else:
            
            result.append(char)
    
    return ''.join(result)


def collatz(n):
    length = 1 
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # If n is even, divide  2
        else:
            n = 3 * n + 1  # If n is odd, multiply  3 and add 1
        length += 1  
    return length

