age=int(input("enter your age : "))
if 8<age<14:
    print("congratulations you are free")
elif 14<age<=30:
    print("your ticket price is rs 200")
elif 30<age<=50:
    print("your ticket price is rs 350")
elif 51<=age<=100:
    print("your ticket price is rs 100")
else:
    print("you cannot watch this movie ")