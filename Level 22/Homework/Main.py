# 2) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა რიცხვი, 
# ხოლო ამ ფუნქციამ უნდა დაბეჭდოს 1-დან გადმოცემულ რიცხვამდე ყველა რიცხვი
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(11)


# 3) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი,
#  ხოლო ამ ფუნქციამ უნდა დააბრუნოს პირველი რიცხვი აყვანილი მე-2 რიცხვის ხარისხში
def multiplying (num1, num2):
    result = num1 ** num2
    return result

result = multiplying(10,2)
print(result)