password = ("goa123")
user_pass = ""

tries = 3
while tries > 0 and user_pass != password:
    user_pass = input("enter your password, you have "+ str(tries)+ " " "tries left: " )
    tries -= 1
if user_pass == password:
    print("welcome to your account") 
elif tries == 0:
    print("youve lost your tries")       
else: print(" access denied ")

