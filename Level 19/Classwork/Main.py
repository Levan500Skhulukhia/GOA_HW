# 1) შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. 
# გადაუარეთ ამ საის while loop-ის გამოყენებით. გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი, 
# საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი

numbers = [3,50,66,77,86,2,43,9,71,42,106]
index = 0
even_sum = 0
odd_sum = 0
while index != (len(numbers)):
    if numbers[index] % 2 == 0:
        even_sum += numbers[index]
    else:
        odd_sum += numbers[index]  
    index += 1

if even_sum > odd_sum:
    print(f"even_sum is greater: {even_sum}")
elif even_sum == odd_sum:
    print("they are equal.")     
else:
    print(f"odd_sum is greater: {odd_sum}")       

# 2) შექმენით სიმბოლოების სია, გადაუარეთ მას for loop-ით და 
# სიიდან ყველა სიმბოლოს შორის მოახდინეთ კონკადინაცია. ციკლის 
# გარეთ დაგჭირდებათ ცვლადი სადაც შაამატებთ ამ სთრინგებს
chars = ["volkswagen", "mercedes", "bmw", "volvo", "opel", "toyota", "ford"]
sum = ""
for char in chars:
    sum += char
print(sum)    