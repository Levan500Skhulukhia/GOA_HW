def disarium_number(number):
    digits = list(map(int, str(number)))  # Split the number into digits
    sum_of_powers = sum(digit ** (index + 1) for index, digit in enumerate(digits))
    return "Disarium  !!" if sum_of_powers == number else "Not !!"


def most_frequent_item_count(array):
    if not array:  # Check if the array is empty
        return 0
    return max(array.count(item) for item in set(array))


def max_multiple(divisor, bound):
    return bound - (bound % divisor)


def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        # Convert the number to a string to iterate over digits
        digits = list(map(int, str(num)))
        # Calculate the sum of digits raised to their respective positions
        if sum(d ** (i + 1) for i, d in enumerate(digits)) == num:
            result.append(num)
    return result

# Examples:
print(sum_dig_pow(1, 10))   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_dig_pow(1, 100))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
print(sum_dig_pow(90, 100)) # Output: []
