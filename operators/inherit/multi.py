# class grand_father:
#     def __init__(self,name,address,number):
#         self.name=name
#         self.address=address
#         self.number=number
#     def details_grand_father(self):
#         print(f"my grand_father is {self.name}")
#         print(f"my grand_father is {self.address}")
#         print(f"my grand_father is {self.number}")

# class father(grand_father):
#     def __init__(self,name,address,number):
#         self.name=name
#         self.address=address
#         self.number=number
#     def details_father(self):
#         print(f"my father_name is {self.name}")
#         print(f"my father_address is {self.address}")
#         print(f"my father_number is {self.number}")

# class son(father):
#     def __init__(self,name,address,number):
#         self.name=name
#         self.address=address
#         self.number=number
#     def details_son(self):
#         print(f"my son_name is {self.name}")
#         print(f"my son_address is {self.address}")
#         print(f"my son_number is {self.number}")

# you_want=eval(input(f"press 1 for grand_father, press 2 for father, press 3 for son,:  "))


# if you_want in (1,2,3):

#     name=(input('enter your name: '))
#     address=(input('enter yoyr address: '))
#     number=eval(input('enter the number: '))

#     obj=son(name,address,number)

#     if you_want==1:
#         obj.details_grand_father()
#     elif you_want==2:
#         obj.details_father()
#     else:
#         obj.details_son()
# else:
#     print('sorry')




      