# append()	
# Adds an element at the end of the list

# my_list=[1,2,3,4,5,6,7,8,9]
# my_list.append(1000)
# print(my_list)
# my_list.append(10)
# print(my_list)

# my_list=[1,2,3,4,5,6,7,8,9]
# new=[]
# for i in my_list:
#     if i <5:
#         new.append(i)
# print(new)


# my_list=[1,2,3,4,5,6,7,8,9]
# my_list.append([22,33,44])
# print(my_list).
# print(my_list[-1])


# my_list=[1,2,3,4,5,6,7,8,9,3,9,5]
# new5=[]
# new9=[]
# for i in range(len(my_list)):
#     if my_list[i] in (5,9):
#         if my_list[i]==5:
#             new5.append(i)
#         else:
#             new9.append(i)
# print(f"this is the 5th list {new5}\n this is 9th list {new9}")


# my_list=[10,29,38,57,66,9,8,8,4,5,38]
# new=[]
# for i in my_list:
#     if i <18:
#         if i not in new:
#             new.append(i)
# print(new)




# copy()	
# Returns a copy of the list

# my_list=[1,2,3,4,5,6,7,8,9]
# a=my_list.copy()
# print(a)

# my_list=[2,3,4,5,6,7,8]
# a=my_list.copy()
# print(a)

# count()
# 	Returns the number of elements with the specified value
# my_list=[1,2,3,4,5,6,7,8,9,5,4,5,4,4]
# print(my_list.count(5))

# my_list=[1,2,3,4,5,6,7,8,9]
# print(my_list.count(5))

# my_list=[22,33,44,5,6,7,8,92,3,4,5,2,3,4,4]
# print(my_list.count(5))


# extend()
# 	Add the elements of a list (or any iterable), to the end of the current list

# my_list=[1,2,3,4,5,6,7,8,9]
# my_list.extend([22,33,44])
# print(my_list)
# b=([99,88,77])
# my_list.extend(b)
# print(my_list)

# my_list=[1,2,3,4,5,6,7,8,9]
# my_list.append([11,55])
# print(my_list)
# my_list.extend([11,22,33,44])
# print(my_list)

# my_list=[2,3,4,5,6,7]
# b=[1,2,3111]
# my_list.extend(b)
# print(my_list)

# my_list=[2,3,4,5,6,7]
# my_list.extend([11,223])
# print(my_list)



# index()
# 	Returns the index of the first element with the specified value
# my_list=[1,2,3,4,5,6,7,8,9,1,1,1,1,5]
# print(my_list.index(5,9))

# my_list=[1,2,3,4,5,6,7,8,9,1,1,1,1,5]
# for i in range(len(my_list)):
#     if my_list[i]==1:
#         print(i,end=' ')

# my_list=[10,20,30,40,50,60,70,10,20,30,40,10,20,30,10,20,10]
# for i in range(len(my_list)):
#     if my_list[i]==10:
#         print(i)

# print(my_list.index(10,5))
# print(len(my_list))

# insert()

# 	Adds an element at the specified position

# my_list=[1,2,3,4,5,6,7,8,9]
# my_list=['anvesh','bittu','chinna','gpi']
# my_list.insert(3,'gopi_raj')
# print(my_list)

# my_list=['anvesh','bittu','chinna','gpi']
# my_list[3]='gopi'
# print(my_list)

# my_list=['anvesh','bitu']
# my_list.insert(4,'gopi')
# print(my_list)

# my_list=['anvesh','bittu','chinna','gpi']
new=[]
# my_list[3]='gopi'
# print(my_list)
# my_list.insert(3,'gopi')
# print(my_list)

# for i in my_list:
#     if i.startswith('g'):
#         i='gopi'
#         new.append(i)
#     else:
#         new.append(i)
# print(new)

# pop()	

# Removes the element at the specified position
# my_list=[1,2,3,4,5,6,7,8,9]
# print(my_list.pop(5))
# print(my_list.index(5))

# my_list=[1,2,3,4,5,6,7,8,9,3,9,5]
# new5=[]
# new9=[]
# for i in my_list:
#     if i in (5,9):
#         if i==5:
#             new5.append(i)
#         else:
#             new9.append(i)
# print(f"this is the 5th list {new5}\n this is 9th list {new9}")




# remove()
# Removes the item with the specified value
# remove()	
# Removes the item with the specified value


# my_list=[1,2,3,4,5,6,7,8,9,5,3,9,5]
# if my_list.count(5) >=3:
#     first=my_list.index(5)
#     second=my_list.index(5,first+1)
#     my_list.pop(second)
# print(my_list)



# my_list=[1,2,3,4,5,0,9,8,7,6,0,10,11,0,12,13]
# for i in range(len(my_list)):
#     if my_list[i]==0:
#         my_list.remove(my_list[i])
#         my_list.append(my_list[i])
# print(my_list)

# my_list=[1,2,3,4,5,0,9,8,7,6,0,10,11,0,12,13]
# for i in my_list:
#     if i==0:
#         my_list.remove(i)
#         my_list.append(i)
# print(my_list)



# my_list=[1,2,3,4,5,6,7]
# print(my_list.remove(7))
# my_list.remove(7)
# print(my_list)

# my_list=[1,2,3,4,5,0,9,8,7,6,0,10,11,0,12,13]
# for num in my_list:
#     if num==0:
#         my_list.remove(num)
#         my_list.append(num)
# print(my_list)


# def table(num):
#     for i in range(1,11):
#         print(f"{num} X {i} = {num*i}")
# while True:
#     num=eval(input('emter the number: '))
#     table(num)



# my_list=[10,9,6,7,2,3,5]
# my_list.sort(reverse=True)
# print(my_list)
# my_list.reverse(True)
# print(my_list)


######################################
# names=['anvesh','chinna','bittu','gopi']
# names.append('leo')
# print(names)
# b=names.copy()
# print(b)

# names.append([11,22,33])
# print(names)

# b=[11,22,33]
# names.extend(b)
# print(names)\


# nums=[1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,366,77,88,99]
# # print(nums.index(1,12))
# for i in range(len(nums)):
#     if nums[i]==1:
#         print(i)


# nums.remove(1)
# print(nums)


# for i in range(len(nums)):
#     if i==1:
#         nums.remove(i)
# print(nums)



# nums=[1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,366,77,88,99]
# c=[]
# for i in nums:
#     if i ==1:
#         nums.remove(1)
#     else:
#         c.append(i)
# print(c)




