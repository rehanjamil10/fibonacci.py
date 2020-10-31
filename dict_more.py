# user_info = {'name':'rehan jamil','age':24,'weight':65}
# print(user_info.get('name'))
# print(user_info.get('names','not found !!!'))
# print(user_info)


# CUBE FINDER
def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes
print(cube_finder(10))