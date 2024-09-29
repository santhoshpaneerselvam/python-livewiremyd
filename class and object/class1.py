
class newclass:
    k=7
    def __init__(self,name):
        self.name=name
        print("santhosh")
    def print(self):
        print(self.name)


obj=newclass("keerthi")
print(obj.k)
obj.print()
obj1=newclass("new")
print(obj1.k)
obj1.k=45
print(obj,obj1.k)






