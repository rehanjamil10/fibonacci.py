# user_info={
#     'name':'rehan',
#     'age':24,
#     'fav_movie':'kkkg',
#     'fav_singer':'edward_maya'
# }

user_info ={}
name=input("enter your name : ")
age=input("enter your age : ")
fav_movies=input("enter your fav_movies using comma  : ").split(',')
fav_tunes=input("enter your fav_tunes : ").split(',')

user_info['name']=name
user_info['age']=age
user_info['fav_movies']=fav_movies
user_info['fav_tunes']=fav_tunes

for key,value in user_info.items():
    print(f'key is {key} : and value is {value}')

# print(user_info)

