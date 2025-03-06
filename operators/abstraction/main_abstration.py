# from abc import ABC,abstractmethod
# class vechile(ABC):
#     def __init__(self,name):
#         self.name=name
       
#     @abstractmethod
#     def start(self):
#         pass

# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def start(self):
#         pass



from abc import ABC,abstractmethod

class vehicle(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def start(self):
        pass







