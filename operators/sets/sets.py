# name={1,2,3,4,5,6,72,3,4,5}
# print(name)
# print(name[1])

# name={'anvesh','bittu','chinna','bittu'}
# num={1,2,3,4,53,4,5}
# values={False,True,1}
# print(name)
# print(num)
# print(values)

# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# names=set(('anvesh','bittu','chinna'))
# new=[]
# for i in names:
#     if i=='anvesh':
#         i='anvesh_bhai'
#         new.append(i)
#     else:
#         new.append(i)
# print(new)

# print(type(names))

# names=set(('anvesh','bittu','chinna'))
# new=[]
# for i in names:
#    new.append(i.capitalize())
# print(new)
    

# names=set(('anvesh','bittu','chinna'))
# new=[i.capitalize() for i in names ]
# print(new)

# Add Items
# names={'anvesh','bittu','chinna','bittu'}
# names.add('sujji')
# print(names)

# update()	|=	Update the set with the union of this set and others

# names={'anvesh','bittu','chinna','bittu'}
# numbers={1,2,3,4,5,6,7}
# names.update(numbers)
# print(names)

# names={'anvesh','bittu','chinna','bittu'}
# num=[1,2,3,4,5,6,7,8]
# names.update(num)
# print(names)

# Python Set remove() Method

# names={'anvesh','bittu','chinna','bittu'}
# to_remove=set()
# for i in names:
#     if i=='bittu':
#         to_remove.add(i)

# names-=to_remove
# print(names)


# names={'anvesh','bittu','chinna','bittu'}
# a=names.pop()
# print(a)
# print(names)

# add()	 	Adds an element to the set

# names={'anvesh','bittu','chinna','bittu'}
# names.add('sujji')
# print(names)


# issubset()	<=	Returns whether another set contains this set or not

# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9}
# c=a.issubset(b)
# print(c)


# interset :
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6,7,8,9,10,11}
# c=a.intersection(b)
# print(c)


