class father:
    def __init__(self,name,address,number):
        self.name=name
        self.address=address
        self.number=number
    def details(self):
        print(f"my father_name is {self.name}")
        print(f"my father_address is {self.address}")
        print(f"my father_number is {self.number}")


class son(father):
    def __init__(self, name, address, number):
        super().__init__(name, address, number)
    
    def details_son(self):
        print(f"my name is {self.name}")
        print(f"my address is {self.address}")
        print(f"my number is {self.number}")

you_want=eval(input('press 1 for father, 2 for son'))
name=(input('enter your name: '))
address=(input('enter yoyr address: '))
number=eval(input('enter the number: '))

obj=son(name,address,number)
if you_want==1:

    obj.details()
else:
    obj.details_son()

