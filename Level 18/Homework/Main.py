# 2)  შექმენით string-ების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ 
# სიაში არსებული ყველა სიტყვის სიმბოლოთა რაოდენობა
words = ["toyota", "volkswagen", "bmw", "mercedes", "volvo", "renault"]

for word in words:
    print(f"{word}: {len(word)} ")


# 3) შექმენით რიცხვების სია, while loop-ის გამოყენებით
#  გაიგეთ ამ სიაში ყველა ლუწი რიცხვის ჯამი და დაპრინტეთ

numbers = [1,4,6,7,55,44,334,75,7,8,44,3,10]   
index = 0
even_number = 0
while index < (len(numbers)):
    if numbers[index] %2 == 0:
        even_number += numbers[index]
    index += 1
print(even_number)


# 4) შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ]
# ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე

names = ["levan", "nika", "arvelodi", "goga", "ani", "amira"]
for name in (names):
    if name[0] == "a":
        print (name)

# # 5) შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. 
# გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი 
# რცხვების ჯამი, რომლებიც არ მეორდება სიაში

chars = [ 1,1,1,1,1,2,2,2,2,5,5,4,4,44,44,]
filtered_char = []
for char in chars:
    if filtered_char.count(char) == 0:
        filtered_char.append(char)
print(filtered_char)        

# 6) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და 
# დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა მარტივ რიცხვს
# ფუნქცია მარტივი რიცხვების დასადგენად

def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False 
    return True  


number = int(input("enter any number: "))


print(f"from 1 to {number} is")
for i in range(1, number + 1):
    if is_prime(i):
        print(i)

# 7) შექმენით სია შემდგარი 5 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტები
words2 = ["toyota", "volkswagen", "bmw", "mercedes", "volvo", ]
print (words2 [2:4:1])

# 8) შექმენით რიცხვების სია, შემდგარი 10 ელემენტისგან.
#  slicing-ის გამოყენებით დაბეჭდეთ სიის ყოველი მეორე ელემენტი

num1 = [ 1,2,3,4,5,6,7,8,9,10]
print (num1 [1::2])

# 9) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ 
# სთრინგის ბოლო სამი სიმბოლო(გამოიყენეთ slicing და მინუსიანი ინდექსები)
exp_str = "alamanterra"
print (exp_str[-3:])

# 10) შექმენით რიცხვების სია, დაბეჭდეთ სია თავიდან ბოლომდე slicing-ის გამოყენებით 
num5 = [ 1,2,3,4,5,6,7,8,9,10]
print (num5[0:10])
