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



def even_fib(n):
    a, b = 0, 1
    total = 0
    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total



def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result



def bouncing_ball(h, bounce, window):
    if h <= 0 or not (0 < bounce < 1) or window >= h:
        return -1
    
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window:
            count += 1
    return count
