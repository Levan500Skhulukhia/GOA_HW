def reverse_bits(n):
    # Convert the number to binary, remove the '0b' prefix, and reverse the string
    reversed_binary = bin(n)[2:][::-1]
    # Convert the reversed binary string back to an integer
    return int(reversed_binary, 2)


def move_zeros_in_place(array):
    index = 0

    # გავიაროთ მასივი და გადავაადგილოთ არა-ნულოვანი ელემენტები წინ
    for num in array:
        if num != 0:
            array[index] = num
            index += 1

    # დავაყენოთ ნულები დარჩენილ ადგილებში
    while index < len(array):
        array[index] = 0
        index += 1

    return array