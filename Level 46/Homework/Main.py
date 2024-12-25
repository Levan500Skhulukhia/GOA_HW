def reverse_bits(n):
    # Convert the number to binary, remove the '0b' prefix, and reverse the string
    reversed_binary = bin(n)[2:][::-1]
    # Convert the reversed binary string back to an integer
    return int(reversed_binary, 2)




def spot_diff(str1, str2):
   
    differences = []
    
    # Iterate over the strings comparing characters at each position
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differences.append(i)  #   Append the index where characters differ
    
    return differences
