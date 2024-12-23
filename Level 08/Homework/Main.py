# გამოიტანეთ თქვენი სახელი და გვარი იმდენჯერ, რამდენი წლისაც ხართ
age = 16
for i in range(age):
    print("levan skhulukhia")

# გამოიტანეთ ტერმინალში რიცხვები 1-დან 20-ის ჩათვლით
for x in range (1, 21):
    print (x)


# გამოიტანეთ ტერმინალში რიცხვები 20-დან 0-მდე
for y in range (20, -1, -1):
    print(y)

# გამოითვალეთ 1-დან 50-ის ჩათვლით ყველა რიცხვის ჯამი და დაპრინტეთ საბოლოო შედეგი
num1=0
for n in range(50):
    num1 = num1 + n
    print(num1)

# დაბეჭდეთ 1-დან 5-ის ჩათვლით რიცხვთა კვადრატი(n * n)
for f in range(1, 6):
    print(f * f)


# დაბეჭდეთ ყველა ლუწი რიცხვის ჯამი 1-დან 10-ის ჩათვლით
sum_even = 0
for c in range(1, 11):
    if c % 2 ==0:
        sum_even += c
print(sum_even)


# მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ცვლადში, შემდეგ კი 0-დან შემოტანილი რიცხვის ჩათვლით შეამოწმეთ,
# თუ ლუწია დაბეჭდეთ რიცხვი is Even, 
# სხვა შემთხვევაში რიცხვი is Odd;(მაგალითად 4, ლუწია ამიტომაც დაბეჭდავთ "4 is Even
number = int(input("type any number: "))
if number % 2 ==0:
    print(f"{number} is Even")
else: print(f'{number} is odd')