#  1) while ციკლის გამოყენებით დაპრინტეთ 1-დან 50-მდე ყველა 4-ის ჯერადი რიცხვის კუბი

num = 1
total_sum = 0
while num < 50:
    if num %4 == 0:
        total_sum += num
    num += 1
if total_sum > 0:
    cube = total_sum ** 3
    print (cube)        


# შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz"
#  და გვერდზე მიუწერეთ რიცხვი. თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" და გვერდზე მიუწერეთ რიცხვი, 
# ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" და გვერდზე მიუწერეთ რიცხვი  

for i in range(1,100):
    if i %3 == 0 and i %5 == 0:
        print("FizzBuzz"+ " "+ str(i))
    elif i %5 == 0:
        print("Buzz"+" "+ str(i))
    elif i %3 == 0:
        print("Fizz"+" "+ str(i))    

# შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი, 
# მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი    

even_sum = 0
for i in range(1,20+1):
    if i %2 == 0:
        even_sum += i

odd_sum = 0
for x in range(1,20+1):
    if x %2 != 0:
        odd_sum += x

even_cube = (even_sum ** 5)
odd_cube = (odd_sum ** 5)
if even_cube > odd_cube:
    print (even_cube)
elif even_cube < odd_cube:
    print (odd_cube)
else:
    print("they are even")                


# 4) True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 <--- 
# გაიგეთ რას გამოიტანს ეს კოდი და ახსენით რატომ.
                   #true            #true              #false        #true       
print (True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5)
# მიუხედავად იმისა, რომ 123 == "123" არის False, სხვა ნაწილები მაინც აძლევს საბოლოო True-ს.

# 5) მომხარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ის მარტივი, თუ მარტივია დაპრინტეთ "Number is prime", 
# სხვა შემთხვევაში "Number is not prime"(მარტივია რიცხვი, რომელიც იყოფა მარტო თავის თავზე და ერთზე)
number = int(input("enter any number: "))
if number > 1:  
    for i in range(2, number):  
        if number % i == 0:  
            print("number is not prime")
            break
    else:  
        print("number is prime")
else:
    print("number is not prime")
