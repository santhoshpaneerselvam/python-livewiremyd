
class employee:
    def __init__(self,name,ID,salary,project):
      
        self.name=name
        self.ID=ID
        self.salary=salary
        self.project=project

#method to print employee's details
    def show_sal(self):

            
            print("name:",self.name,"salary:",self.salary,'ID:',self.ID)

    def proj(self):
        print(self.name,'is working on',self.project)

#creating object of a class
emp=employee('harish',123,15000,'IT company')
#calling public method of the class
emp.show_sal()
emp.proj()     


class students:
    def __init__(self,name,rank,points):
        self.name=name
        self.rank=rank
        self.points=points

    def gettername(self):
        print(self.name)

    def settername(self,name):
        self.name=name

str1=students("keerthi",5,132)

str1.gettername()
str1.settername("santhosh")
str1.gettername()


class employee:
    def __init__(self,name,ID,salary,project):
        self.name=name
        self.ID=ID
        self.salary=salary
        self.project=project

    def show(self):
        print("name:",self.name,"ID:",self.ID,"salary:",self.salary)

    def value(self):
        print(self.name,'completed in project ',self.project)

emp=employee('navin',25656,25000,'IT company')

emp.show()
emp.value()

