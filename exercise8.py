# number = list(range(1,21))
# reverse_list= number[::-1]
# print(reverse_list)

# def reverse_list(l):
#     return l[::-1]
# # number= [1,2,3,4,5,6]
# number= list(range(1,21))
# print(reverse_list(number))
# print(number.pop())

# def reverse_list(l):
#     return l[::-1]
# string = ['rehan','shazia','nazia','nasreen']
# print(reverse_list(string))
# print(string.pop())

def reverse_list(l):
    r_list=[]
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
numbers = list(range(1,21))
print(reverse_list(numbers))