def compute_sum(n):
    
    total_sum = 0  # This will store the total sum of digits

    # Loop through all numbers from 1 to n
    for number in range(1, n + 1):
        # Convert the number to a string to access each digit
        for digit in str(number):
            total_sum += int(digit) 

    return total_sum



    