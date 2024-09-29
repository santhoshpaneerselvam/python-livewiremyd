
class Eagle:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def var (self):
        print(f"I am Eagle, my name is {self.name}. I am {self.age}years old.")
    def sound (self):
        print("scream")


class Duck:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def var (self):
        print(f"I am Duck, my name is {self.name}. I am {self.age}years old.")
    def sound (self):
        print("quack")


class sparrow:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def var (self):
        print(f"I am sparrow, my name is {self.name}. I am {self.age}years old.")
    def sound (self):
        print("chirp")


Eagle1=Eagle("kite",5)
Duck1=Duck("duckling",3)
sparrow1=sparrow("chick",2)
for bird in (Eagle1,Duck1,sparrow1):
    bird.sound()
    bird.var()



