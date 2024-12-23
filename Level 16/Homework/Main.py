# 2) შექმენით სია სადაც გექნებათ რიცხვები. 
# for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი

numbers = [1, 3, 55, 4, 101]
max_number = numbers [0]

for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)    

# 3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი


numbers1 = [1, 3, 55, 4, 101]

def factorial (n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


for number in numbers1:
    fact = factorial(number)
    print (fact)


# 4) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი
numbers2 = [1, 3, 55, 4, 101]
min_number = numbers [0]

for number in numbers:
    if number < min_number:
        min_number = number
print(min_number)    


# 5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები,
#  შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი
#  რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).

numbers3 = [1, -5, -7, -23, 3, 55, 4, 101]

neg_numbers = []
i = 0
while i < len(numbers3):
    if numbers3[i] < 0:
        neg_numbers.append(numbers3[i])
    i += 1

print (neg_numbers)        

# 6) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range()
#  ფუქნცია ან შექმენით ცვლადი)
# 1. შექმენით რიცხვების სია
numbers4 = [1, 2, 3, 4, 5]


for i in range(len(numbers4) - 1, -1, -1):  
    print(numbers4[i])  

# 7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია
#  სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
words = ["n", "n", "l", "l", "r", "r"]
words = list(set(words))
print (words)



# 8) შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი 
# ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის
word = "yamaha"

invers = word[::-1]

print(invers)


# 9) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, 
# სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი

num = int(input(" enter any number: "))
divisors = [0]
for i in range(1,num+1):
    if num %i == 0:
        divisors.append(i)

print (divisors)        


# შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს
#  და დაპრინტავს რომელი საუკუნეა ის

year = int(input("enter any year: "))
if year % 100 == 0:
    century = year // 100
else:
    century = year // 100 + 1
print(str(century) + "-th century")    