mixed = [1,2,3,4,5,'rehan','shazia','nazia']
mixed.append('tiger')
print(mixed)

fruits=[]
fruits.append('mango')
fruits.append('grapes')
print(fruits)


# to add element to a particular position #INSERT METHOD
fruits=['mango','grapes','guava','litchi']
animals=['tiger','lion','man','monkey']
fruits.insert(1,'orange')
print(fruits)
summation= fruits+animals
print(summation)

# EXTEND METHOD
animals.extend(fruits)
animals.append(fruits)
print(animals)
fruits.append(animals)
fruits.extend(animals)
print(fruits)
