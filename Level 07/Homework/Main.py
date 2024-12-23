w1 = 50
w2 = ('tesla')
w3 = 2.0

print (type (w3))
print (type (w2))
print (type (w1))

number1 = int(input('write any number: '))
print (type(number1))

print (40 <= 24)
print(38 > 37)
print(1 > 1.0)
print(50 == 50.0)
print(2.4 > 2)
print(7 > 6) 
print(-15 > 53)
print(2.4 > 77)
print(20 < 12)
print(51 == 51)

# "AND"
print(4 > 3 and 5 > 1)
num = 15 > 20 and 40 < 11
print (num)
num2 = 15 > 20 and 40 > 11
print(num2)
num3 = 20 > 15 and 40 > 11
print (num3)

# "OR"
print(4 > 3 or 5 > 1)
num4 = 15 > 20 or 40 < 11
print (num4)
num5 = 15 > 20 or 40 > 11
print(num5)
num6 = 20 > 15 or 40 > 11
print (num6)


age = input("type your age: ")
print (type(age))

age_int = int(age)
print (type(age_int))

age_float = float(age)
print (float(age_float))


fav_num = int(input("type your favorite number: "))
if fav_num % 2 == 0:
    print ("that is even number")
else:
    print(' thats odd number')  


my_name_is = ('levan')

user_name = input('type your name: ')
user_age = int(input('type your age: '))

if user_age >= 18:
    print('you are adult')
else:
    print('you are kid') 

if user_name == my_name_is:
    print('we have same names:D')       
else:
    print('you have different name')    