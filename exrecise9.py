def reverse_list(l):
    empty_list = []
    for i in l:
        empty_list.append(i[::-1])
    return empty_list
lists = ['abc','cde','xyz']
print(reverse_list(lists))