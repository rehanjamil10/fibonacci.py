def filter_odd_even(l):
    even_nums = []
    odd_nums = []
    for i in l:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [even_nums, odd_nums]
    return output
num = list(range(1,21))
# num = [1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(num))