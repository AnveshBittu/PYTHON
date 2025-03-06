    # names=['anvesh','bittu','chinna']
    # numbers=[9700022751,9110565034,8465951152]
    # converting=dict(zip(names,numbers))
    # print(converting)


# names={'chinna':123,'bittu':222,'gopi':9090}
# # print(names.get('chinna'))


# get()
# 	Returns the value of the specified key

# names={'chinna':123,'bittu':222,'gopi':9090}
# print(names.get('chinna'))
# names={'chinna':123,'bittu':222,'gopi':9090}


# try:
#     print(names['bittuuu'])
# except KeyError:
#     print('sorry')
# # try:


#     print(names.get('bittuuu'))
# except :
#     print('sorry')



# keys()	
# Returns a list containing the dictionary's keys

# names={'chinna':123,'bittu':222,'gopi':9090}

# kes=names.keys()
# converting=list(kes)
# # print(converting)
# converting.insert(1,'okok')
# print(converting)

# print(names.keys())



# print(tuple(names.keys()))


# names={(1,2,3,4):'anvesh, bittu,chinna,gopi',(5,6,7):'ok1,ok2,ok3'}

# data=names.keys()
# converting=list(data)
# # print(converting)
# converting.pop([1,2,3,4])
# print(converting)



# print(names[(1,2,3,4)])



# data=names[(1,2,3,4)]
# converting=list(data)
# print(converting)



# items()
# 	Returns a list containing a tuple for each key value pair


# names={'chinna':123,'bittu':222,'gopi':9090}
# print(names.values())
# print(tuple(names.values()))



# pop()	Removes the element with the specified key

# names={'chinna':123,'bittu':222,'gopi':9090}
# # print(names.pop('chinna'))
# names.pop('chinna')
# print(names)



# values()
# 	Returns a list of all the values in the dictionary

# names={'chinna':123,'bittu':222,'gopi':9090}
# names.update({'leo':99988877})
# print(names)


# names={'chinna':123,'bittu':222,'gopi':9090}
# names.update({'chinna':222222})

# print(names)



################################lop########################
# while True:
#     data={}
#     name=input('enter the name: ')
#     price=eval(input('enter the price: '))
#     data[name]=price
#     print(data)


########## nexted########
# details={
#     'bittu':{'name':'bittu','number':9800,'address':'guntur'},
#     'chinna':{'name':'chinna','number':8465951152,'address':'balaji nagar'},
#     'gopi':{'name':'gopi','number':8121665666,'address':'tpk'},
#     'leo':{'name':'leo','number':100,'address':'guntur_old'},
    
# }
# # print(details['bittu']['address'])
# print(details['leo']['number'])




#############################################


# def find(name):
#     count={}
#     for i in name:
#         if i not in count:
#             count[i]=1
#         else:
#             count[i]+=1
#     print(count)
# num=input('enter the number: ')
# find(num)

# def find():
#     name=input('enter the name: ')
#     name.split()
#     count={}
#     for i in name:
#         if i not in count:
#             count[i]=1
#         else:
#             count[i]+=1
#     print(count)
# find()

