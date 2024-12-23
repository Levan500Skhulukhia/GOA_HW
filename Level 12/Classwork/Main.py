num1 = int(input("enter first number: "))  # შევქმნათ პირველი ცვლადი
num2 = int(input(" enter second number: "))  # მერე მეორე
sum = num1 + num2 # ვაჯამებთ ორ ცვლადს
sum_cube = (sum ** 3)   # ვიყვანთ კუბს
if sum_cube %2 == 0: # ვამოწმებთ იყოფა თუ არა იგი 2-ზე ნაშთის გარეშე
    print("its even number.") # თუ იყოფა გამოაქვს რომ ლუწია
else:
    print("thats odd number.")    # თუ არა და კენტია