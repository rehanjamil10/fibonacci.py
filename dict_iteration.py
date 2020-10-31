# in keyword and iterations in dictionary
user_info={
    'name':'rehan',
    'age':24,
    'fav_movie':'kkkg',
    'fav_singer':'edward_maya'
}
# check if key exist in dictionary

# if 'age' in user_info:
#     print("present")
# else:
#     print("not present")


# check if value exist in dictionary

# if 'rehan' in user_info.values():
#     print("present")
# else:
#     print("not present")


# loops in dictionary

# for i in user_info:      #-----> for keys
#     print(i)
    

# for i in user_info.values():    #-----> for values
#     print(i)



# values method

# user_info=user_info.values()
# print(user_info)
# print(type(user_info))


# for i in user_info.keys():
#     print(i)


# items method

# user_items=user_info.items()
# print(user_info)
# print(type(user_info))


# for key,value in user_info.items():
#     print(f' key is {key} and value is {value}')

# how to add data to dict

# user_info['height'] = 6.2
# print(user_info)

# pop method()

# poppped = user_info.pop('name')
# print(user_info)
# print(poppped)


# pop item method

# poppped_item= user_info.popitem()
# print(user_info)
# print(poppped_item)
# print(type(poppped_item))



# update method

more_info={'name1':'nazia','state': 'bihar','hobbies':['reading','coding','playing guitar']}
user_info.update(more_info)
print(user_info)  
print(type(user_info))
# print(more_info.update(user_info))    #SYNTAX ERROR



