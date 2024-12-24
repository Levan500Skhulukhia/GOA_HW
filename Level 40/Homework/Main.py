def sum_digits(number):
   
    number = abs(number)
    
    
    digits = [int(digit) for digit in str(number)]
    
    # Step 3: Sum the digits
    return sum(digits)



def solution(nums):
    # Check if the input is None or empty, return an empty list in such cases
    if not nums:
        return []
    # Sort the array in ascending order
    return sorted(nums)



def high(x):
    
    words = x.split()
    
    # ინიციალიზაცია მაქსიმალური ქულისა და სიტყვისთვის
    max_score = 0
    best_word = ""
    
     #ყველა სიტყვის ქულის გამოთვლა
    for word in words:
        score = 0
        for char in word:
            # ასოს ქულის გამოთვლა: a=1, b=2, ..., z=26
            score += ord(char) - ord('a') + 1
        
        # თუ ქულა მაქსიმალურია, შევინახოთ ახალი საუკეთესო სიტყვა
        if score > max_score:
            max_score = score
            best_word = word
    
    return best_word