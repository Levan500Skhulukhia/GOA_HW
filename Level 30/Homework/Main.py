# 2) შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია

# 3) შექმენით ფუნქცია manual_len, რომელსაც გადაეცემა სთრინგი ან სია, ხოლო ფუნქციამ უნდა დააბრუნოს გადმოცემული სთრინგის/სიის სიგრძე(არ გამოიყენოთ len-ი)

# 4) შექმენით ფუნქცია manual_pop, რომელსაც გადაეცემა ორი არგუმენტი, სია და ინდექსი. წაშალეთ სიიდან, გადმოცემულ ინდექსზე მყოფი ელემენტი. საბოლოოდ კი დააბრუნეთ ეს სია(არ გამოიყენოთ .pop ფუნქცია)

car_brands = ["Toyota", "Honda", "Ford", "BMW", "Mercedes-Benz", "Audi", "Chevrolet", "Nissan", "Hyundai", "Kia"]

car_brands.pop(2)
car_brands.insert(0,"volvo")
print (car_brands)

def manual_len(object):
    count_len = 0
    for i in object:
        count_len += 1
    return count_len

print(manual_len([1,2,3,4,5]))    
print(manual_len("vaxo"))

def manual_pop(array, num):
    array = array[:num] + array[num+1:]
    return array

print(manual_pop(car_brands, 5))