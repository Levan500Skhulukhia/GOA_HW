# 2) for ციკლით მომხარებელს შემოატანინეთ 5 ელემენტი სიაში და დაბეჭდეთ სია

# შექმენი ცარიელი სია
friends = []

# for ციკლი 5 ელემენტის დამატებისთვის
for i in range(5):
    name = input(f"enter {i+1}- friends name: ")  # მიიღეთ სახელი
    friends.append(name)  # დაამატეთ სახელი სიაში

# დაბეჭდეთ სია
print("friend list: ", friends)

# 3) შექმენით ხილების სია, სადაც გექნებათ მინიმუმ 3 ელემენტი. მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი, 
# თუ სიის ბოლო ელემენტის ინდექსი არის ლუწი ჩაამატეთ შემოტანილი ხილი სიაში, სხვა შემთხვევაში არ ჩაამატოთ 

# შევქმენი სია
fruits = ["apple", "banana", "cherry", ]
# შევქმენი მომხმარებლის მიერ შემოყვანილი ხილი
fav_fruit = input("enter your favorite fruit: ")
# ვუწესებ პირობებს
if len(fruits) %2 != 0:
    fruits.append(fav_fruit)
    print(fruits) 
else:
    print("sorry bro")    

# 4) შექმენით სია შემდგარი სახელებისგან. მომხარებელს შემოატანინეთ მისი სახელი, 
# თუ მისი სახელი იქნება 5 სიმბოლოს ტოლი ან მეტი. 
# ჩაამატეთ სიაში, სხვა შემთხვევაში დაუბეჭდეთ "Name is too short"

# შევქმნათ სია
names = ["giga", "soso", "temuri", "arvelodi", "ucha"]
user_name = input(" enter your name: ") # შემოვატანინოთ მომხმარებელს სახელი
if len(user_name) >= 5: # ვუწერ პირობას და ვამოწმებ
    names.append(user_name) # ვამატებ სიაში
    print(names)
else:
    print(" your name is too short.")    


# 5) შექმენით სია შემდგარი 10 ელემენტისგან. დაპრინტეთ ის და მომხარებელს შემოატანინეთ რიცხვი 1-დან 10-ჩათვლით.
# შემდეგ წაშალეთ სიის ის ელემენტი რომელი რიცხვიც გადმოგეცათ და დაპრინტეთ განახლებული სია
number_list = ["volvo", "mercedes", "bmw", "honda", "alfa-romeo", "nissan", "subaru", "ford", "volkswagen", "opel"]
user_schoose = input(" enter which car you want to buy (1-10): ")
if user_schoose == "1":
    del number_list[0]
elif user_schoose == "2":
    del number_list [1]
elif user_schoose == "3":
    del number_list [2]
elif user_schoose == "4":
    del number_list [3]     
elif user_schoose == "5":
    del number_list [4]
elif user_schoose == "6":
    del number_list [5]
elif user_schoose == "7":
    del number_list [6]
elif user_schoose == "8":
    del number_list [7]
elif user_schoose == "9":
    del number_list [8]
elif user_schoose == "10":
    del number_list [9]                    

else: 
    print("we dont have that type of car")
print(number_list)    

#6) კომენტარებით ახსენით რა არის ინდექსი და მოიყვანეთ მაგალითი

#ინდექსი არის სიის ან სტრინგის ელემენტების პოზიცია.
#Python-ში ინდექსი იწყება 0-დან.
#ნეგატიური ინდექსები საშუალებას იძლევა სიის ელემენტების წვდომა უკუკერძისაგან.

cars = ["volvo", "mercedes", "bmw", "honda", "alfa-romeo"]

# 0 ინდექსზე არის "volvo"
print(cars[0])  # შედეგი: volvo

# 2 ინდექსზე არის "bmw"
print(cars[2])  # შედეგი: bmw

# 4 ინდექსზე არის "alfa-romeo"
print(cars[4])  # შედეგი: alfa-romeo
