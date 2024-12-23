run = False
while not run:
    user_input = input(" how are you?  ")

    if user_input.lower() == "normal":
        print(" i hope you will get beter!  ")
        run = True
    elif user_input.lower() == "great":
        print("thats good, have a nice day! ")
        run = True
    elif user_input.lower() == "bad" or user_input.lower() == "super sad":
        print(" its sad :( ")
        run = True
    else:
        print(" i dont understand, repeat please. ")
        continue
    print("good bye! ")

