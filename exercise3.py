                                       #NESTED IF ELSE
guessed_number = int(input("enter your guessed number between 0 to 30 : "))
winning_number = 14
if winning_number== guessed_number:
    print("congratulations you won this game")
else:
    if guessed_number > winning_number:
        print("guessed num is too high ")
    if guessed_number < winning_number:
        print("guessed num is too low ")