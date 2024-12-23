# მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ,
#  რამდენჯერ შედის შემოტანილი რიცხვი 100-ში. გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)

num = int(input(" enter any number: "))
print (100 // num)


# while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამი

sum_numbers = 0
num1 = 1
while num1 < 20:
    if num1 %2 != 0:
        sum_numbers += num1
    num1 += 1

print (sum_numbers)        


# მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, 
# რომელიც არის მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal

number1 = int(input(" enter first number: "))
number2 = int(input(" enter second number: "))
if number1 > number2:
    print("first number is greater.")
elif number2 > number1:
    print("second number is greater.")
else:
    print(" both are equal.")       

# მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის ფაქტორიალი(დასერჩეთ რა არის ფაქტორიალი)

def factorial (n):
    if n == 0:
        return 1

    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result   
    
number = int(input(" enter number: "))    

print (f"{number} factorial is - {factorial(number)}")

# მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. 
# შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი

number5 = int(input("enter any number: "))

squares = 0
for i in range(1,number5+1):
    squares += i**2

print(f"from 1 to {number5} is : {squares}")    


#თამაში "რიცხვის გამოცნობა". შექმენით ცვლადი და შეინახეთ რომელიმე რიცხვი 1-დან 20-ის ჩათვლით(ეს იქნება ჩაფიქრებული რიცხვი)
# . გამოიყენეთ while loop-ი და მომხარებელს შემოატანინეთ რიცხვი იქამდე სანამ არ გამოიცნობს მას. 
# თუ მომხარებლის მიერ შემოტანილი რიცხვი მეტია ჩაფიქრებულზე, დაპრინტეთ To high, თუ ნაკლებია Too low,
#  ხოლო იმ შემთხვევაში თუ მომხარებელი გამოიცნობს რიცხვს დაპრინტეთ "You win"

guess = ()
while guess !=(11):
    guess = int(input("guess my number: "))
    if guess > 11:
        print(" too high")
    elif guess < 11:
        print(" too low")   
    else: print(" YOU WON")     