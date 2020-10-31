#TAKE TWO COMMA SPARATED INPUT FROM USER
# EX USERS NAME , A SINGLE CHARACTER
# OUTPUT
# USERS NAME LENGTH
# COUNT THE CHARACTER

name,char = input("enter your name and a character using comma separation : ").split(",")
print(f"length of your name is {len(name)}")
print(f"length of your character {name.lower().count(char.lower())}") #CASE SENSITIVE
# print(name.lower().count(char.lower()))
