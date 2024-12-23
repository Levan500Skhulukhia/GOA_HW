# 1) შექმენით ფუნქიცა, manual_find, რომელსაც გადაეცემა არგუმენტად სთრინგი და ერთი სიმბოლო, რომელიც უნდა ვიპოვოთ ამ სთრინგში. თუ სიმბოლო მოიძებნა დააბრუნეთ მისი ინდექსი, სხვა შემთხვევაში დააბრუნეთ -1

#2) შექმენით ფუნქცია manual_count, რომელსაც არგუმენტად გადაეცემა რიცხვბის სია, და ერთი რიცხვი, რომლის რაოდენობაც უნდა ვიპოვოთ ამ სიაში. დააბრუნეთ მიღებული რაოდენობა

def manual_find(word, letter):
    for index, char in enumerate(word):   # Use enumerate to get the index
        if char == letter:
            return index  #Return the index of the first match
    return "-1" # Return -1 if no match is found

print(manual_find("alamantera","a"))        


def manual_count(array,num): 
    count = 0  # makin the count variable
    for i in array:  
        if i == num: # if i == num count will raise for 1
            count += 1
    return count

print(manual_count([3,3,2,5,7,66,4,3,10.], 5))        