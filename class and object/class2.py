class employee:
    def __init__(self,name,age,salary):
        self.name=name 
        self.age=age
        self.salary=salary
        print("salary is increase in monthly")
    def read (self):
        print(self.name,self.age,self.salary)
    def __str__(self):
        return str(self.age)

obj=employee("keerthi",26,10000)

print(obj)


