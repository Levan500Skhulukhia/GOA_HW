#2) შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.

#გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step



def manual_range(start, end=None, step=1):
    
    if end is None:
        end = start
        start = 0

    # Initialize an empty list to store the result
    result = []

    # Create the range manually using a while loop
    if step > 0:
        while start < end:
            result.append(start)
            start += step
    elif step < 0:
        while start > end:
            result.append(start)
            start += step
    else:
        raise ValueError("step must not be zero")

    return result


print(manual_range(5))        

# 4) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს string-ს. ამ ფუნქციამ უნდა გაიგოს გადმოცემულ string-ში თითოეული სიმბოლოს რაოდენობა და ჩაამატოს ახალ სიაში(ერთი სიმბოლის რაოდენობა მხოლოდ ერთხელ უნდა ჩაამატოთ. მგალითად თუ string-ში 5 "a" გვხვდება, რიცხვი 5 მასივში მხოლოდ ერთხელ უნდა ჩავამატოთ, მაგრამ სხვა სიმბოლოც თუ გვხვდება იგივე რაოდენობით, მას ვამატებთ ჩვეულებრივ). საბოლოდ დაასორტირეთ მიღებული სია ზრდადობით და დააბრუნეთ

def count_unique_frequencies(s):

    counts = []
    
    # თითოეული სიმბოლოს დათვლა
    for char in s:
        found = False
        for item in counts:
            if item[0] == char:  # თუ სიმბოლო უკვე სიაშია
                item[1] += 1
                found = True
                break
        if not found:  # თუ სიმბოლო სიაში ჯერ არ არის
            counts.append([char, 1])
    
    # უნიკალური რაოდენობების სიის შექმნა
    unique_counts = []
    for item in counts:
        if item[1] not in unique_counts:  # თუ რაოდენობა ჯერ არ არის სიაში
            unique_counts.append(item[1])
    
    # სორტირება
    unique_counts.sort()
    return unique_counts

print(count_unique_frequencies("boombom"))


# 5) შექმენთ ფუნქცია, რომელიც არგუმენტად იღებს სიმბოლოების სიას. დაასორტირეთ ეს სია ანბანის მიხედვით, გადააქციეთ string-ად და დააბრუნეთ
def sorting_symbols(array):

    sorted_array = sorted(array) # დავასორტიროთ ანბანის მიხედვით
    
    result = "".join(sorted_array) # ვაქცევტ სტრინგად და მოვახდენთ კონკადინაციას
    return result

print(sorting_symbols(["b","a","c","x,","f"]))

#6) შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვების სიას და აბრუნებს მას კლებადობის მიხედვით დასორტირებულს
def sorting_reverse(array):
   
    sorted_array = sorted(array, reverse=True) # ვალაგებთ კლებადობით
    return sorted_array

print(sorting_reverse([1,5,4,6,3,7]))