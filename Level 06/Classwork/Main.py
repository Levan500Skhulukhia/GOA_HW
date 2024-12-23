firstname = input('type your firstname: ')
surname = input('type your surname: ')
age = input('type your age: ')
mail = input('type your mail: ')

num1 = int(input( 'choose first number: '))
num2 = int(input('choose second number'))
print(num1 + num2)
print(num1 - num2) 
print(num1 * num2)
print(num1 / num2)


# project dumb calculator
print ('welcome to dumb calculator')
n1 = int (input('Type number 1: '))
n2 = int (input('Type number 2: '))

action =  input('what do you wanna do?   \  + 1 plus \n - minus \n / divide \n * multiply \n')
if action == '+':
    print(n1+n2)
elif action == '-':
    print(n1-n2)
elif action == '/':
    print(n1/n2)
elif action == '*':
    print(n1*n2)  
else: print("bro are you dumb or something?")         

