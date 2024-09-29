
class person:
    def __init__(self,name1,name2):
        self.firstname=name1
        self.lastname=name2
    def printname(self):
        print(self.firstname,self.lastname)


class college (person):
    def __init__(self,name1,name2,college):
        super().__init__(name1,name2)
        self.college=college
    def printn(self):
        print(self.firstname,self.lastname,self.college)


class student (college):
    def __init__(self,name1,name2,college,degree):
        super().__init__(name1,name2,college)
        self.degree=degree

k=student("harish","kumar","avc","b.com")
k.printname()
k.printn()
print(k.degree)



class base1():
    def __init__(self):
        self.str1="s"
        print("flower")

class base2():
    def __init__(self):
        self.str2="p"
        print("bird")

class derived(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("forest")
    def printstrs(self):
        print(self.str1,self.str2)

obj=derived()
obj.printstrs()


