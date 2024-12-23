# 6) შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. 
# საბოლოოდ დაპრინტეთ ეს სია(გამოიყენეთ for loop)
# number = []
for index in range (1,100):
    if index %2 == 0:
        number.append(index)

print (number)

# 7) შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. 
# შემდეგ გადაუარეთ for loop-ით და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი.
# საბოლოოდ დაპრინტეთ მიღებული სია

numbers = list(range(1, 51))

filtered_numbers = [number for number in numbers if number % 2 == 0]

print(filtered_numbers)

# 8) შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი,
#  while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე
#  სანამ სიაში არ დარჩება ორი ელემენტი. ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია

fruits = ["apple", "banana", "orange", "kiwi", "grape", "mango", "pear", "peach", "pineapple", "strawberry"]
while len(fruits) != 2:
    fruits.pop(-1)
    print (fruits)

# 9) შექმენით პროგრამა, რომელიც დაითვლის თუ რამდენჯერ 
# შედის სიაში რიცხვი 1 numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] 
# (ამისათვის გადაუარეთ სიას for loop-ით)
numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] 
count = 0
for number in numbers:
    if number == 1:
        count += 1

print (count)        

# 10) შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით 
# მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა. 
# თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში, 
# სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია

list1 = []
list2 = []
for i in range(5):
    words = input("enter anything: ")
    if len(words) < 5:
        list1.append(words)
    else:
        list2.append(words)   

print(list1)
print(list2)