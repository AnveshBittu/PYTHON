# anvesh=lambda a,b,:a+b*a-b
# print(anvesh(10,20))

# filter
# my_list=[2,3,4,5,6,7,8,11,22,33,32,1,16,19,16,19,33,44]
# new=[]
# for i in my_list:
#     if i>=18:
#         new.append(i)
# print(new)


# def filter1(num):
#     return num>=18

# my_list=[2,3,4,5,6,7,8,11,22,33,32,1,16,19,16,19,33,44]
# res=filter(filter1,my_list)
# print(list(res))


# my_list=[2,3,4,5,6,7,8,11,22,33,32,1,16,19,16,19,33,44]
# res=filter(lambda a:a>=18,my_list)
# print(list(res))


# def plus(num): 
#     return num+10

# my_list=[10,20,30,40]

# res=list(map(lambda a: a+10,my_list))
# print(res)
# from functools import reduce

# def redu(num,num1):
#     return num+num1

# my_list=[10,20,30,40]
# res=reduce(lambda a,b:a+b,my_list)
# print(res)



# def prime(num):
#     if num>=1:
#         for i in range(2,num):
#             if num % i==0:
#                 return 'not prime'
#         return 'it prime'
#     return 'sorry'
# while True:
#     num=eval(input('enter your number: '))
#     print(prime(num))


# prime=list(filter(lambda a: all( a%i!=0 for i in range(2,a)),range(1,101)))
# print(prime)




# my_list=[10,20,30,40]
# new=[]
# for i in my_list:
#     if i < 20:
#         new.append(i)
# print(new)
    

# def fil(my_list):
#     return my_list >20

# my_list=[10,20,30,40]
# res=list(filter(fil,my_list))
# print(res)


# my_list=[10,20,30,40]
# res=list(filter(lambda a: a>20,my_list))
# print(res)