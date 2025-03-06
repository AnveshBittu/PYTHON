# lst1=[10,20,30,40]
# las2=[1,2,3,4]
# for i,j in zip(lst1,las2):
#     res=i+j
#     print(res,end=' ')




# names=['anvesh','chinna','gopi','nani']
# keys=[1,2,3,4]
# res=dict(zip(keys,names))
# print(res)

# num1=eval(input('enter the num1 that you want: '))
# num2=eval(input('enter the num2 that you want: '))

# print(f"before swap num1 is {num1} num2 is {num2}")

# temp=num1
# num1=num2
# num2=temp

# num1,num2=num2,num1

# num1=num1+num2 #10+20=30 actual num is 10
# num2=num1-num2 #30-20=10   ##10
# num1=num1-num2 #30-10=20 ##20

# print(f"after swap num1 is {num1} num2 is {num2}")


# lst=['anvesh','chinna','gopi','nani',22,33,44,66]
# names=[]
# num=[]
# for i in lst:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         num.append(i)
# print(num,names)

# class father:
#     def __init__(self):
#         print('hi bittu')
#     def bittu_info(self):
#         print('my name is bittu how r u')
# class son(father):
#     def __init__(self):
#         print('hi anvesh')
#     def anvesh_info(self):
#         print('my name is anvesh how r u')
# obj=son()



data={}
res=input(f"if you want to processed yes 1 or exit 2")

if res==1:
    name=input('enter the name: ')
    price=eval(input('enter the number: '))
    data[name]=price
if res == 2:
    break
print(data)
