def solve(s):
    max_sum = 0
    current_sum = 0
    
    for char in s:
        if char not in 'aeiou':
            current_sum += ord(char) - ord('a') + 1
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    
    return max(max_sum, current_sum)




def filter_string(st):
    return int(''.join([char for char in st if char.isdigit()]))





def highest_rank(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_freq = max(freq.values())
    most_frequent_numbers = [key for key, value in freq.items() if value == max_freq]
    return max(most_frequent_numbers)




def up_array(arr):
    if not arr or any(d < 0 or d > 9 for d in arr):
        return None
    
    num = int(''.join(map(str, arr))) + 1
    return [int(digit) for digit in str(num)]
