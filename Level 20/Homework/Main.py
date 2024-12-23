# 2) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი 
# და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Nika").
#  გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი

def introdution(name):
    print("hello"+ " " + name)


# name = ("Levan")

introdution("levan")

introdution("Zviad")


# 3) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 რიცხვი.
#  ფუნქციამ უნდა დაბეჭდოს ამ რიცხვების ნამრავლი. საბოლოოდ გამოიძახეთ ის


def multiply (num1, num2):
    operation = (num1 * num2)
    print(operation)


multiply(5, 5)


# 4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სია. 
# ფუნქციამ უნდა დაბეჭდოს ეს სია შებრუნებულად(არ გამოიყენოთ slicing-ი)
def reverse():
    original_num = [1,2,3,4,5,6,7,8,9]
    reversed_num = list(reversed(original_num))
    print(reversed_num)


reverse()


# 5) შექმენით ფუნქცია, რომელსაც გადასცემთ რიცხვების სიას.
#  გადაუარეთ გადმოცემულ სიას for ციკლით და დააბრუნეთ ახალი სია,
#  სადაც ჩამატებული იქნება გადმოცემული სიიდან მხოლოდ ის რიცხვები,
#  რომლებიც მეტია 10-ზე. საბოლოოდ დააბრუნეთ ეს სია
def big_nums():
    numbers = [1,5,11,24,25,30,77,4,8,9]
    big_numbers = []
    for i in range(len(numbers)):
        if numbers[i] > 10:
            big_numbers.append(numbers[i])
    print(numbers, "in this list")
    print(big_numbers, "this numbers are greater than 10")
       
big_nums()

# 6) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია.
#  ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, 
# გამოიყენეთ slicing-ი

def remove_first_and_last(input_list):
    return input_list[1:-1]


my_list = ['a', 'b', 'c', 'd', 'e']
result = remove_first_and_last(my_list)
print(result)



# 7) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია,
#  გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ
#  სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში),
#  გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ
def calculating (list1, list2):
    list1sum = 0
    list2sum = 0
    for i in  list1:
        list1sum += i
    for x in list2:
        list2sum += x   
    print (list1sum * list2sum)     
    
num1 = [2,3,4,5,4,3,8]
num2 = [65,4,3,7,81]

calculating(num1,num2)

# 8) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
# გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული 
# რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
def double(input_list):
    result = []
    index = 0  
    while index < len(input_list):
        result.append(input_list[index] * 2) 
        index += 1  
    return result

numbers = [1, 2, 3, 4]
doubled_numbers = double(numbers)
print(doubled_numbers)

# 9) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. 
# გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი
#  რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
def filtering (user_list):
    filtered_list = []
    for i in user_list:
        if i %2 == 0:
            filtered_list.append(i)
    return (filtered_list)
        
numbers1 = [1,5,11,24,25,30,77,4,8,9]
even_nums = filtering (numbers1)
print(even_nums)

#10) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. 
# შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული 
# სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. 
# საბოლოოდ დააბრუნეთ ეს სია
def n_names (user_names):
    filtered_names = []
    for i in user_names:
        if i[0] == "N":
            filtered_names.append(i)
    return (filtered_names)    

names = ["Nina", "Nathan", "Nikolai", "Natalie", "John", "Sarah", "Michael", "Emily"]
result = (n_names(names))
print(result)
