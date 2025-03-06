# name='anvesh is good boy'
# print(name)

# name="anvesh is good boy, it's a new ball"
# print(name)

# name='''
# hi anvesh 
# how are you
# r u good
# '''
# print(name.count('o'))
# print(name)







# name='anvesh is good boy'
# print(name.index('z'))
# print(name.find('z'))

# my_list=['anvesh@gmail.com','bittu@gmail.com','chiina@gmail.in']
# com=[]
# inn=[]

# for i in my_list:
#     if i.endswith('com'):
#         com.append(i)
#     else:
#         inn.append(i)

# print(f"this is the com list {com}\n this is the inn_list {inn}")



# my='anvesh is good boy okoko'
# print(my.find('z'))
# print(my.index('z'))


#########################################################################################3

# capitalize()
# 
# 	Converts the first character to upper case

# name='anvesh'
# print(name.upper())


# lower()
# 
# 	Converts a string into lower case

# name='ANWESH'
# print(name.lower())


# count()	
# 
# Returns the number of times a specified value occurs in a string

# name='anvesh is good boy '
# print(name.count('o'))


# find()	

# Searches the string for a specified value and returns the position of where it was found

# name='my name is anvesh okko'
# print(name.find('z'))



# format()	
# 
# Formats specified values in a string
# my_string='my name is {name} , my age is {age}'.format(name='anvesh',age=33)
# print(my_string)

# my_string='my name is {0}, my age is {1}'.format('anvesh',33)
# print(my_string)

# my_string='my name is {}, my age is {}'.format('anvesh',33)
# print(my_string)

# name=['anvesh','bituu','chinna','gopi']
# for i in name:
#     print(f"hi {i} ela unnav ?".format(i))



# isalnum()	Returns True if all characters in the string are alphanumeric

# name='2'
# print(name.isalnum())


# strip()	Returns a trimmed version of the string

# name='   anvesh  '
# print(len(name))
# a=name.strip()
# print(len(a))


# name='    anvesh                '
# print(len(name))
# a=name.lstrip()
# print(len(a))




# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# name="Hello My Name Is PETER"
# print(name.swapcase())


# split()	Splits the string at the specified separator, and returns a list

# name='anvesh is good boy'
# a=name.split()
# # print(a)
# new=[]
# for i in a:
#     if i=='anvesh':
#         i='bittu'
#         new.append(i)
#     else:
#         new.append(i)
# print(new)
# res=' '.join(new)
# print(res)


# def find_occurrence():
#     name=input('enter the string: ')
#     name.split()
#     data={}
#     for i in name:
#         if i not in data:
#             data[i]=+1
#         else:
#             data[i]+=1
#     print(data)
# find_occurrence()


# name='anvesh is good boy'
# a=name.split()
# # print(a)
# # for i in a:
# a.insert(0,'bittu')
# # print(a)
# c=' '.join(a)
# print(c)
#############################################################

# names=['anvesh','bittu','chinna']
# new=[]
# for i in range(len(names)):
#     if names[i] ==names[i]:
#         names[i]=names[i].capitalize()
#         new.append(names[i])
# print(new)


# names='anvesh bittu chinna gopi'
# a=names.split()
# # print(a)
# for i in range(len(a)):
#     a[i]=a[i].capitalize()
# c=' '.join(a)
# print(c)

# name='anvesh bittu chinna'
# a=name.split()
# for i in range(len(name)):
#     a[i]=a[i].capitalize()
# c=' '.join(a)
# print(c)


# names='my name is {name} my age is {age} my address is {address}'.format(name='anvesh',age=2,address='guntur')
# print(names)

# names='my name is {0} my age is {2} my address is {1}'.format('anvsh','guntur',33)
# print(names)

# names='my name is {} my age is {} my address is {}'.format('anvesh',22,'guntur')
# print(names)

# names=['anvesh','chinna','gopi','leo']
# for i in names:
#     print(f"my {i} tinnara ?".format(i))

# import datetime
# def wish():
#     data=datetime.datetime.now()
#     # h=int(data.strftime('%H'))
#     print(data)
# wish()


# from funtions.funtions import anvesh
# print(anvesh())

# from funtions.funtions1 import bittu
# bittu()



########################################

# names='anvesh is good boy'
# print(names.upper())
# print(names.lower())
# print(names.startswith('a'))
# print(names.endswith('y'))
# print(names.count('o'))

# names='      anvesh is good boy   '

# # print(names.replace('anvesh','bittu').replace('good','bad'))
# # print(names.title())
# print(len(names))
# b=names.lstrip()
# print(len(b))

# names=['anvesh','chinna','bittu','gopi']
# for i in names:
#     print(f"hi {i} garu tinnara?".format(i))

# names='anvesh is good boy'
# # a=names.split()
# new=[]
# for i in a:
#     if i=='good':
#         i='bad'
#         new.append(i)
#     else:
#         new.append(i)
# data=' '.join(new)
# print(data)


# names='anvesh is good boy'
# a=names.split()
# for i in range(len(a)):
#     a[i]=a[i].capitalize()
# # print(a)
# new=' '.join(a)
# print(new)
