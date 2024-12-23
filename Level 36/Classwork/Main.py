# # ASC Week 1 Challenge 4 (Medium #1)

# Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

# Note that spaces should be ignored in this case.


def vaporcode(s):
    s = s.replace(" ", "")
    
    return "  ".join(s.upper())

# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
def capitals(word):
    result = []
    for idx, char in enumerate(word):  # Loop with index and character
        if char.isupper():  # Check if the character is uppercase
            result.append(idx)  # Append the index
    return result



# # bThere is a bus moving in the city which takes and drops some people at each bus stop.

# You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

# Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

# Take a look on the test cases.

# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

# The second value in the first pair in the array is 0, since the bus is empty in the first bus stop

def number(bus_stops):
    # Initialize the total number of people on the bus
    total_people = 0
    
    # Iterate through each bus stop's data
    for on, off in bus_stops:
        total_people += on  # Add the number of people getting on the bus
        total_people -= off  # Subtract the number of people getting off the bus
    
    # Return the final number of people on the bus
    return total_people


# write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def count_bits(n):
    # Convert number to binary, count '1's, and return the result
    return bin(n).count('1')

