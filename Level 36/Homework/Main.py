# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))

# ტესტი:
print(digital_root(16))      
print(digital_root(942))     
print(digital_root(132189))  
print(digital_root(493193))  

# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    words = sentence.split() # makes words from strings
    for i in range(len(words)):  # loop for each word
        if len(words[i]) >= 5:  # if word is bigger than 5
            words[i] = words[i][::-1]  # return spinned word
    return ' '.join(words)  