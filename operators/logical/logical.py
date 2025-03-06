# a=[1,2,3,4,5,6]
# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)
# print(a[::-1])




# a.sort()
# print(a[-2])

# a=[0,1,2,3,4,5,0,0,4,5,0,2]
# # new=[]
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(i)

# print(a)


    
# def prime(num):
#     if num >1:
#         for num1 in range(2,num):
#             if num % num1 ==0:
#                 return 'this is not prime'
#         return 'this is prime'
#     return 'this is also not prime'
# while True:
#     num=eval(input('enter the num: '))
#     print(prime(num))



# prime=list(filter(lambda a: all(a%i!=0 for i in range(2,a)),range(1,101)))
# print(prime)




# def fact(num):
#     a=1
#     for i in range(1,num+1):
#         a=a*i
#     print(a)
# fact(5)



# import math

# res=math.factorial(5)
# print(res)

# anvesh=lambda a: a*anvesh(a-1) if a else 1
# print(anvesh(10))


# fact=lambda a: a*fact(a-1) if a else 1
# num=eval(input('enter your number: '))
# print(fact(num))


# fact=lambda a: a*fact(a-1) if a else 1
# print(list(fact))


# reverse a string

# name='anvesh'
# b=''
# for i in name:
#     b=i+b
# print(b)\


# 

# 1) find the number is positive or neg or Zero

# num=int(input('enter your number: '))
# if num>=1:
#     print('this is positive',num)
# elif num ==0:
#     print('this is zero',num)
# else:
#     print('this is nagetive',num)


# 2) find the even num or odd

# num=eval(input('enter the number: '))
# if num % 2==0:
#     print('this is even number',num)
# else:
#     print('this is odd number',num)

# duplicate

# my_list=[10,20,30,40,50,60,60,22,33,44,55,66,40,10]
# new=[]
# dup=[]
# for i in my_list:
#     if i not in new:
#         new.append(i)
#     else:
#         dup.append(i)
# final=sorted(new)
# print(final)
# print(dup)
# new=[]
# for i in my_list:
#     if i not in new:
#         new.append(i)
# print(new)
    
# common 


# list1=[1,2,3,4,5,6,7,8]
# list2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# new=[]
# for i in list1:
#     if i in list2:
#         new.append(i)
# print(new)





# 5)palindrome

# def palindrome(name):
#     if name==name[::-1]:
#         print(f"it is pal : {name}")

#     else:
#         print('not pal')
# while True:
#     name=input('enter the name: ')
#     palindrome(name)

#  6)write a function summ all elements:
# def sum_all(num):
#     total=0
#     for i in num:
#         total+=i
#     print(f"this is the total:{total}")
# my_list=[10,20,30,40]
# sum_all(my_list)

# 6) reverse
# my_list=[10,29,38,48,57,60]
# reverse_table=[]
# for i in range(len(my_list)-1,-1,-1):
#     reverse_table.append(my_list[i])
# print(reverse_table)


# 7)largest element
# my_list=[10,29,38,48,57,60]

# largest=my_list[0]
# for i in my_list:
#     if i>largest:
#         largest=i
# print(largest)
# # largest=0
# for i in my_list:
#     if i >largest:
#         largest=i
# print(largest)

# 8) smallest
# my_list=[10,29,38,48,57,60,5]
# smallest=my_list[0]
# for i in my_list:
#     if i <smallest:
#         smallest=i
# print(smallest)



# 9) add two list by using map lambda
# l1=[10,20,30]
# l2=[20,30,40]
# res=map(lambda a,b:a+b,l1,l2)
# print(list(res))

# 10) table
# def table(num):
#     for i in range(1,11):
#         ans=num*i
#         print(f"{num} X {i} = {ans}")


# while True:
#     num=eval(input('enter the number: '))
#     table(num)


# for i in range(1,101):
#     for j in range(1,11):
#         add=i*j
#         print(f"{i} X {j} ={add}",end='   ')
#     print()
# print()

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}",end=' ')
#     print()


# 11) find accurrance only numbers

# def find_accurrance(num):
#     data={}
#     for i in num:
#         if i in data:
#             data[i]+=1
#         else:
#             data[i]=+1
#     print(data)
# my_list=[1,2,3,4,5,61,2,3,4,51,2,3]
# find_accurrance(my_list)






# 12) find accurrance only string

# def find_accurrance():
#     name=input('enter the char: ')
#     name.split()
#     data={}
#     for i in name:
#         if i in data:
#             data[i]+=1
#         else:
#             data[i]=+1
#     print(data)
# find_accurrance()


# 13) fibanoci numbers

# def fib(num):
#     a=0
#     b=1
#     for i in range(0,num+1):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=' ')
# while True:
#     num=eval(input('enter the number: '))
#     fib(num)






# 14) cap
# name='anvesh bittu chinna'
# # a=name.split()
# for i in range(len(a)):
#     a[i]=a[i].capitalize()
# c=' '.join(a)
# print(c)


    
# my=['anvesh','bittu','chinna']
# for i in range(len(my)):
#     my[i]=my[i].capitalize()
# print(my)

# 15)Check Anagram Strings in Python

# str1=input('enter the string: ')
# str2=input('enter the 2nd string: ')
# if sorted(str1)==sorted(str2):
#     print('this is Anagram')
# else:
#     print('this is not Anagram')

# 16) swap
# num1=eval(input('enter the number1: '))
# num2=eval(input('enter the 2nd number: '))
# print(f"befor swap num1 {num1} and num2 {num2}")

# temp=num1
# num1=num2
# num2=temp
# print(f"after swap num1 {num1} and num2 {num2}")


# 2nd method
# num1=eval(input('enter the number1: '))
# num2=eval(input('enter the 2nd number: '))
# print(f"befor swap num1 {num1} and num2 {num2}")

# num1, num2 = num2, num1
# print(f"after swap num1 {num1} and num2 {num2}")



# 3rd method

# num1=eval(input('enter the number1: ')) #10
# num2=eval(input('enter the 2nd number: '))#20
# print(f"befor swap num1 {num1} and num2 {num2}")

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2

# # num1=num1+num2 #10+20=30
# # num2=num1-num2 # 30-20=10
# # num1=num1-num2 # 30-10=20

# print(f"after swap num1 {num1} and num2 {num2}")


# amstrong
# num=int(input(f"enter the the that you want: ")) #153
# new=num
# lenght=len(str(num)) # 3
# sum=0
# while num!=0: #153 # 15
#     r=num%10 #153%10=3 # 15%10=5
#     sum+=(r**lenght) # 3**3=>3*3*3=27 # 5**5=>5*5*5=125
#     num=num//10 # 153 //10 => 15 # 15 // 10=1
# if new==sum:F
#     print('correct')
# else:
#     print('sorry')



# my_list=[1,2,3,4,5,0,9,0,6,7]
# for i in my_list:
#     if i ==0:
#         my_list.remove(i)
#         my_list.append(i)

# print(my_list)



#  How To Remove Nth occurrence of the word from a List

# my_list=['anvesh','bittu','chinna','anvesh','gopi','anvesh']
# word='anvesh'
# count=0
# n=3
# for i in range(0,len(my_list)):
#     if my_list[i]==word:
#         count+=1
#         if count==n:
#             del my_list[i]
# print(f"after updating: {my_list}")






# How To Clear a List
# my_list=[1,2,3,4,5,6]
# print(f"befor clearing the list {my_list}")
# my_list.clear()
# print(f"after clearing the list {my_list}")


# my_list=[1,2,3,4,5,6]
# print(f"befor clearing the list {my_list}")    
# my_list=[]
# print(f"after clearing the list {my_list}")

# my_list=[1,2,3,4,5,6]
# print(f"befor clearing the list {my_list}") 
# my_list *=0
# print(f"after clearing the list {my_list}")


# Count Occurrences of an element in a list

# my_list=[10,11,19,10,12,15,18,16,10]
# num=10
# count=0
# for ele in my_list:
#     if (ele==num):
#         count+=1
# print(f"{num} count is {count}")



# my_list=[10,11,19,10,12,15,18,16,10]
# num=10
# count=my_list.count(num)
# print(f"{num} count is {count}")

# my_list=[10,11,19,10,12,15,18,16,10]
# num=10
# print(f"{num} count is {my_list.count(num)}")
# my_list=[10,11,19,10,12,15,18,16,10]
# print(f"{num:=10} count is {my_list.count(num)}")
# print(f"{(num:=10)} count is {([10,11,19,10,12,15,18,16,10].count(num))}")


# print(f"{(num:=10)} count is {([10,11,19,10,12,15,18,16,10].count(num))}")




# name=input('enter the name: ')
# res=''.join(reversed(name))
# print(res)



# name='anvesh is anves good'
# d={}
# for i in name:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# for j,k in d.items():
#     print(f"{j} = {k} items".format(j,k))


def display(name):
    def messgae():
        return 'hello'
    result=messgae() +name
    return result
print(display(' anvesh'))