# dictionaries intro
# why we use dictionaries?
# ----> becoz of limitations of lists,lists are not enough to represent real data

#  example 
user = ['harshit',24,['coco','kimi na no wa'],['awakening','fairy tales']]
# this list contains user name , age,fav movies,fav tunes
# you can do this but this is not a good way to do this


# Q----> what are dictionaries?
# A----> unordered collection of data in key :value pair

#  how to create dictionaries
user1={'name':'rehan','age':24,'gender':'male'}
# print(user1)
# print(type(user1))


# second method to create dictionary

user2= dict(name='rehan',age=24,gender='male')
# print(user2)
# print(type(user2))


# how to access data from dictionary
# note- there is no indxing because of unordered collection of data
# what type of data a dictionary can store

user2= dict(name='rehan',age=24,gender='male')
print(user2['gender'])

# what type of data a dictionary can store
# -----> numbers,strings,list,dictionary


user_info={
    'name':'rehan',
    'age':24,
    'fav_movie':'kkkg',
    'fav_singer':'edward_maya'
}
print(user_info)
print(user_info['fav_singer'])


# how to add data to an empty dictionary
user_info2={}
user_info2['name']='mohit'

user_info2['age']=24
print(user_info2)