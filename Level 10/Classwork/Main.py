# მომხარებელს შემოატანინეთ მისი ასაკაი, შეინახეთ ის ცვლადში და შეადარეთ. 
# თუ ასაკი არის ლუზი დაბეჭდეთ თქვენი ასაკი არის ლუწი. სხვა შემთხვევაში: თქვენი ასაკი არის კენტი

age = int(input(" enter your age: "))
if age %2 == 0:
    print (str(age) + " " + "your age is even ")
else: 
    print (str(age) + " " + "your age is odd" )

# გამოიტანეთ 10-დან 50-ის ჩათვლით ყველა ლუწი რიცხვი. გამოიყენეთ for loop-ი

for num in range (10, 50 + 2, 2):
    print (num)