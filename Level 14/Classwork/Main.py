# 2) შექმენით სია სადაც, შეიტანთ მინიმუმ 10 რიცხვს, გადაუარეთ for ციკლის დახმარებით და დაბეჭდეთ თითოეული რიცხვი კენტია თუ ლუწი.

numbers = [1, 2, 55, 6, 77, 3, 47, 99, 100, 201]
odds = []
even = []

for number in  numbers:
    if number %2 == 0:
        even.append(number)
    else:
        odds.append(number)    

print (even, "even numbers")
print (odds, "odd numbers")


# 3) შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან 
# მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი
names = ["levana", "gio", "luka", "dachi", "gvanca", "temuri", "lana", "mate", "kokhora", "dato"]

for index in range(len(names)):
    if index %2 != 0:
        print(names[index])

# 4) შექმენით სია სადაც გექნებათ 10 რიცხვი, თქვენი დავალებაა გაიგოთ ამ სიაში 
# ყველა ლუწი და კენტი რიცხვიოს ჯამი და დაბეჭდოთ

num1 = [4, 5, 6, 8, 44, 76, 50, 3, 123, 77]
even1 = 0
odd1 = 0
for index1 in (num1):
    if index1 %2 == 0:
        even1 += index1
    else:
        odd1 += index1

print(even1, "even")
print(odd1, " odd")            
        
# 5) შექმენით სია სადაც გექნებათ 10 რიცვი, შემდეგ შექმენით ახალი სია, 
# სადაც ჩაამატებთ პირველი სიიდან ყველა ლუწ რიცხვს და გაიგებთ მათ საშუალო არითმეტიკულს.
# (ახალ სიაზე გამოიყენეთ len() ფუნქცია)
num2 = [4, 5, 6, 8, 44, 76, 50, 3, 123, 77]
even_list = []
for number9 in num2:
    if number9 %2 == 0:
        even_list.append(number9)
even_sum = sum(even_list)
print (even_sum)        