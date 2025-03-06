# class father:
#     def work(self):
#         print(f"my father work is plumbing")
# class mother:
#     def work(self):
#         print(f"my mother work is house wife")

# class son(father,mother):
#     pass

# obj=son()
# obj.work()
# mother.work(obj)


class father:
    def __init__(self):
        print(f"hi sekhar")
    def eat(self):
        print('i can eat')
    def sleep(self):
        print('i can sleep')
class mother:
    def __init__(self):
        print('hi sujji')
    def work(self):
        print('i can work')
    def sleep(self):
        print(f"i can sleep mom")

class son(mother,father):
    pass
    # def work_1(self):
    #     print(f"i con work super")
    # def sleep(self):
    #     print(f"i can sleep son")
obj=son()
# print(father(obj))
print(father.mro())