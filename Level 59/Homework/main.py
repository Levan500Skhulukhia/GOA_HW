def lowercase_count(strng):
    return sum(1 for char in strng if char.islower())



def digitize(n):
    return [int(digit) for digit in str(n)][::-1]



def merge_arrays(arr1, arr2):
      return sorted(set(arr1 + arr2))





def collatz(n):
    length = 1 
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # If n is even, divide  2
        else:
            n = 3 * n + 1  # If n is odd, multiply  3 and add 1
        length += 1  
    return length



def DNA_strand(dna):
     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
     return ''.join(complement[base] for base in dna)



def tail_swap(strings):
    first_part1, second_part1 = strings[0].split(":")
    first_part2, second_part2 = strings[1].split(":")
    return [f"{first_part1}:{second_part2}", f"{first_part2}:{second_part1}"]





def row_weights(array):
    team1 = sum(array[i] for i in range(0, len(array), 2))
    team2 = sum(array[i] for i in range(1, len(array), 2))
    return (team1, team2)



def mine_location(field):
     for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                return [i, j]



def compute_sum(n):
    
    total_sum = 0  # This will store the total sum of digits

    # Loop through all numbers from 1 to n
    for number in range(1, n + 1):
        # Convert the number to a string to access each digit
        for digit in str(number):
            total_sum += int(digit) 

    return total_sum