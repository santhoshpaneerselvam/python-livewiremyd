
class firstclass:
    s=15
    def func(self,name):
        self.name=name
        print("cricket")
    def printl(self):
        print(self.name)


new=firstclass()
print(new.s)
new.func("santhosh")
new.printl()
new1=firstclass()
print(new1.s)
new1.s=2006
print(new,new1.s)

