
class school:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print ("system moving on data")
    def funschool(self):
        print(self.name,self.age,self.place)

k=school("santhosh",18,"mayiladuthurai")
k.funschool()


class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print ("salary is increase in monthly")

    def work(self):
        print(self.name,self.age,self.salary)

    def __str__(self):
        return str(self.age)


obj=employee("keerthi",18,25000)
obj.work()
print (obj)



