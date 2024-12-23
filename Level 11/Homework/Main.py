# განსაზღვრავს secret_pass - სწორი პაროლი, რომელიც უნდა შეიყვანოს მომხმარებელმა.
# secret_pass = "luka1234"
# user_pass ინიციალიზდება ცარიელი სტრიქონით, რადგან მომხმარებლის პაროლი ჯერ არ არის შეყვანილი.
# user_pass = ''

#tries ინიციალიზაცია 3-ით, რაც ნიშნავს, რომ მომხმარებელს შეუძლია 3 მცდელობა.
# tries = 3

# while ციკლი, რომელიც მომუშავეა მანამ, სანამ მცდელობების რაოდენობა არ განულდება
# ან სანამ პაროლი არ იქნება სწორად შეყვანილი
# while tries > 0 and user_pass != secret_pass:
    # მომხმარებელს სთხოვს პაროლის შეყვანას და აჩვენებს, რამდენი მცდელობა დარჩა
    # user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
    
    # მცდელობების რაოდენობის შემცირება
    # tries = tries - 1

    # თუ მომხმარებელმა სწორად შეიყვანა პაროლი
    # if user_pass == secret_pass:
        # დაბეჭდავს "Access granted!", რომ მომხმარებელს წვდომა აქვს
        # print("Access granted!")
    # თუ მცდელობები დასრულდა
    # elif tries == 0:
        # დაბეჭდავს შეტყობინებას, რომ მცდელობები ამოიწურა
        # print("You've reached the maximum number of tries. Access denied!")
    # სხვა შემთხვევაში, როდესაც პაროლი არასწორია, მაგრამ მცდელობები ჯერ არ ამოიწურა
    # else:
    #     # დაბეჭდავს "Access denied! Try again."
    #     print("Access denied! Try again.")




# დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)

count = 0

for num in range(1,50+1):
    if num %2 == 0:
        count += 1
print(count)        

# დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. 
# გამოიყენეთ while loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)

count1 = 0
even_sum = 0

num1 = 1
while num1 <=100:
    if num1 %2 == 0:
        even_sum += num1 
        count1 += 1
    num1 += 1
if count1 > 0:
    average = even_sum / count1 
    print(average)        


# დაბეჭდეთ ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზე(გამოიყენეთ while loop-ი)

sum1 = 0
num5 = 1
while num5 <= 30:
    if num5 %3 ==0:
        sum1 += num5
    num5 += 1
print(sum1)    


# მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)
N = int(input("type any number: "))
for i in range (1, N+1):
    if N %i == 0:
     print(i)        


# დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია
number11 = int(input(" type any number: "))
if number11 > 0:
    print(" thats positive number.")
elif number11 < 0:
    print("thats negative number.")
else: 
    print("thats zero.")        


#დაწერეთ პროგრამა, 
# რომელიც მომხარებელს შემოატანინებს წელს და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც თებერვალში 29 დღე გვაქვს).
#  ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.(გამოიყენეთ and და or ოპერატორები)

year = int(input("type any year: "))
if (year %4 == 0 and year % 100 != 0) or year % 400 == 0:
    print (" thats leap year.")
else:
    print("that is not leap year")    

# მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით (ეს იქნება მისი ქულა).
#  თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", თუ 80-დან 90-მდე, გამოუტანეთ 
# "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D"

grade = int(input("enter your grade: "))
if grade >= 90 and grade <= 100:
    print(" your grade is A")
elif grade >= 80 and grade < 90:
    print(" your grade is B") 
elif grade >= 70 and grade < 80:
    print("your grade is C")
elif grade < 70:
    print(" your grade is D")
else:
    print("system error - invalid grade")              