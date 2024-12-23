#  შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ რიგით მერამდენეა ის.

# მგალითად: "Hello" >>> "H - 1", "e - 2"..

char = "scorpion" 
index = 1
for i in char:
    print(i + "-" + str(index)) # თთო იტერაციის შემდეგ იზრდება ინდექსი ერთით.
    index += 1


# 2) შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. ამ ფუნქციამ უნდა შეართოს ეს სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი

def manual_join(string_list, separator):
   
    result = ""
    
    # 2. თუ სია ცარიელია, უბრალოდ დააბრუნე ცარიელი სტრინგი
    if len(string_list) == 0:
        return result
    
    # 3. გავდივართ სიას და გავაერთიანებთ სტრინგებს
    for i in range(len(string_list)):
        # პირველი ელემენტი, უბრალოდ დავამატოთ
        if i == 0:
            result += string_list[i]
        else:
            result += separator + string_list[i]
    
    return result

print(manual_join(["boom", "baam", "aaaa",], "-"))

# 3) შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ან სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ. დააბრუნეთ მიღებული შედეგი.
def manual_count(char):
    count = 0   # შევქმნათ ცვლადი სადაც შევინახავთ ელემენტების რაოდენობას
    for i in char:
        count += 1  # გადავუარეთ ფორ ციკლით და ვუმატებთ თითო იტერაციის შემდეგ ემატება ერთი
    return count
print(manual_count("alamntera"))    


# 4) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.

def manual_replace(array, char1, char2):
    # 1. ვაკეთებთ სიაზე ჩამოწერას
    array = list(array)  # თუ ის სტრინგია, აქ ვაქცევთ მას სიად

    for i in range(len(array)):
        if array[i] == char1:
            array[i] = char2  # შეცვლის ელემენტს ადგილობრივად
    
    return ''.join(array)  # სიას ვაქრობთ ისევ სტრინგად

print(manual_replace("hello levan wassup", " ", "-"))


