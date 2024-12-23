# კონკადინაცია არის ორი სტრინგის შეერთება, მაგალითად
word1 = ('world')
word2= ('class')
print (word1 + word2)


num1 = input('Choose number, 1,2,3,4,5,6,7: '  )
if num1 == '1':
    print('monday')
elif num1 == '2':
    print('tuesday')
elif num1 == '3':
    print('wednesday')
elif num1 == '4':
    print('thursday')    
elif num1 == '5':
    print('friday')
elif num1 == '6':
    print('saturday')
elif num1 == '7':
    print('sunday')         
else: print ('ERROR BROO!')


a = int(input("type first number: "))
b = int(input('type second number: '))
if a > b:
    print ('first is greater')
elif a < b:
    print ('second is greater')
else: print('they are equal') 


age = int(input('type your age: '))
if age > 18:
    print('you are adult')
elif age< 18:
    print('you are a kid')



num2 = int(input('type first number'))
num3 = int(input('type second number'))
num4 = int(input('type third number'))
num5 = int(input('type fourth number'))
number_list = (num2 + num3 + num4 + num5)
result = (number_list / 4)
print(result)


# int-integer არის რაიმე რიცხვი რის მეშვეობიტაც შეგვილია რამე მათემატიკური მაგალიტი გავაკეთოთ
print(30+40)
print(20/5)
print(5*5)

# str-string არის ისეთი რამ რაც კომპიუტერი კითხულობს როგორც სიმბოლოებს, ასოებს
print('levana is a good boy')
print('Yeah buddy'+' '+"lightweight!")
print('arwivi vnaxe dawrili yvav-yornebs eomeboda')