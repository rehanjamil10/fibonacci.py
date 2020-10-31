def common_finder(l1,l2):
    output1 = []
    for i in l1:
        if i in l2:
            output1.append(i)
        
    return output1

# num1 = list(range(1,21))
# num2 = list(range(8,16))
print(common_finder([1,2,3,4,5],[3,4,5,6,7]))