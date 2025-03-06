# from main_abstration import vehicle

# class bike(vehicle):
#     def __init__(self,model):
#         # super().__init__(name)
#         self.model=model
        

#     def start(self):
#         print('i can start with kick')
#         print(f"my bike name is {self.model}")


# class scooty(vehicle):
#     def __init__(self,model):
#         # super().__init__(name)
#         self.model=model
        

#     def start(self):
#         print('i can start with self')
#         print(f"my scooty name is {self.model}")

# class car(vehicle):
#     def __init__(self,model):
#         # super().__init__(name)
#         self.model=model
        

#     def start(self):
#         print('i can start with key')
#         print(f"my car name is {self.model}")
        














# # class bike(vechile):
# #     def __init__(self,name,model):
# #         super().__init__(name)
# #         self.model=model
# #     def start(self):
# #         print('i can start with kick')
# #         print('my bike model is :',self.model)


# # class car(vechile):
# #     def __init__(self,name,model):
# #         super().__init__(name)
# #         self.model=model
# #     def start(self):
# #         print('i can start with key')
# #         print('my car model is :',self.model)


# # class scooty(vechile):
# #     def __init__(self,name,model):
# #         super().__init__(name)
# #         self.model=model
# #     def start(self):
# #         print('i can start with self')
# #         print('my scooty model is :',self.model)


from main_abstration import vehicle
class bike(vehicle):
    def __init__(self, name,model):
        super().__init__(name)
        self.model=model

    def start(self):
        print(f"i can drive with kick")
        print('my bike model is',self.model)


class car(vehicle):
    def __init__(self, name,model):
        super().__init__(name)
        self.model=model

    def start(self):
        print(f"i can drive with key")
        print('my bike model is',self.model)
        print(f"my car name is {self.name}")

