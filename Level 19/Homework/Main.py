# 1) შექმენით სია შემდგარი მინიმუმ 5 ელემენტისგან.
#  წაუშალეთ ამ სიას ბოლო ორი ელემენტი და დაბეჭდეთ ის
chars = ["volkswagen", "mercedes", "bmw", "volvo", "opel", "toyota", "ford"]

chars.pop(6)
chars.pop(5)
print(chars)

# 2) შექმენით ცვლადი, სადაც შეინახავთ სთრინგს. slicing-ის მეშვეობით დაბეჭდეთ ის უკუღმა
word = "vakhobrooklyn"
print (word[::-1])

# 3) შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. 
# გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი
numbers = [1,43,54,3,5,6,78,8,7,5,69,99]
smallest = numbers[0]
greatest = numbers[0]
sum_of_numbers = (greatest + smallest)

for number in numbers:
    if number < smallest:
        smallest = number
    elif number > greatest:
        greatest = number

sum_of_numbers = (greatest + smallest)
print (sum_of_numbers)        


# 4) შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, 
# არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა,
#  რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)
word = "racecar"

if word == word[::-1]:
    print(" it's a palindrome!")
else:
    print("it's not a palindrome.")


# 5) შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით,
#  გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში 
# და დაბეჭდეთ მათი რაოდენობა
numbers1 = [1,43,54,3,5,6,78,8,7,5,69,99]
even_num = 0
odd_num = 0
for num in numbers1:
    if num %2 == 0:
        even_num += 1
    else:
        odd_num += 1

print (even_num, "even numbers")
print (odd_num, "odd numbers")

# 6) შექმენით სია, სადაც გექნებათ 1-ანები და 0-ანები, შექმენით ახალი სია,
#  რომელიც თავიდან იქნება ცარიელი. for loop-ით გადაუარეთ პირველ სიას და თუ
#  საიტერაციო ცვლადის მნიშვნელობა იქნება 1, ახალ სიაში ჩაამატეთ True, სხვა შემთხვევაში
#  False. საბოლოოდ დაბეჭდეთ ახალი სია

sec_num = [1,1,0,1,0,0,1,1,0,1,0,]

result = []
for num1 in sec_num:
    if num1 == 1:
        result.append(True)
    elif num1 == 0:
        result.append(False)
    else:
        print("error")    

print(result)