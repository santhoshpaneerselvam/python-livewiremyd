
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)


class student (person):
    pass
x=student("santhosh","vishal")
x.printname()





class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)


class student (person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        person.__init__(self,fname,lname)
        self.graduationyear=2024


x=student("sakthi","arjun")
print(x.graduationyear)
x.printname()


'''

class person1:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)


class student1 (person1):
    pass
x=student1("mani","hari")
x.printname()





class person1:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)


class student1 (person1):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        person1.__init__(self,fname,lname)
        self.place=trichy

x=student1("bala","ramana")
print(x.place)
x.printname()

'''
    
