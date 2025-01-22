def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    return [i + 1 for i, letter in enumerate(word) if letter in vowels]





def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors






def more_zeros(s):
    result = []
    seen = set()
    
    for char in s:
        if char not in seen:
            binary_representation = bin(ord(char))[2:]  
            zeros = binary_representation.count('0')
            ones = binary_representation.count('1')
            if zeros > ones:
                result.append(char)
            seen.add(char)  
    
    return result






def arrays_similar(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    count1 = {}
    count2 = {}
    
    for elem in arr1:
        count1[elem] = count1.get(elem, 0) + 1
    
    for elem in arr2:
        count2[elem] = count2.get(elem, 0) + 1
    
    return count1 == count2