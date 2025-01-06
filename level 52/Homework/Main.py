def gimme(input_array):
    sorted_array = sorted(input_array)
    middle_value = sorted_array[1]
    return input_array.index(middle_value)




def sum_of_minimums(numbers):
    total = 0
    for row in numbers: 
        total += min(row)
    return total





def two_oldest_ages(ages):
    ages.sort()
    if ages[-1] == ages[-2]:
        return [ages[-2], ages[-1]]
    else:
        return [ages[-2], ages[-1]]



def even_fib(n):
    a, b = 0, 1
    total = 0
    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
