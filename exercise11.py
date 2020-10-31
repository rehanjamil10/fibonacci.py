def sublist_counter(l):
    count = 0
    for i in l:
        if type(i)== list:
            count+=1
    return count
mixed = [1,2,[2,3],'rehan',[5,6],[8,9]]
print(sublist_counter(mixed))