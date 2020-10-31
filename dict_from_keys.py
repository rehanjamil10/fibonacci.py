# FROM KEYS
d = {'name':'unknown','age':'unknown'}

# d=dict.fromkeys(['name','age','height','weight'],'unknown')

# d=dict.fromkeys(('abc'),'unknown')

# d=dict.fromkeys(range(1,11),'unknown')

# print(d)


# get method (useful)
d = {'name':'rehan','age':'unknown'}
# print(d['name'])
# print(d.get('age'))    # get method syntax

# if 'names' in d:
#     print('present')
# else:
#     print('not present')


# if d.get('name'):
#     print('present')
# else:
#     print('not present')

d1=d.copy()
print(d1)
