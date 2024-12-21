m=input("do you have a medical condition")
a=int(input("enter your attendence"))
if m=="y":
    print("your allowed")
else:
    if a>75:
        print("you are allowed")
    else:
        print("you are not allowed")