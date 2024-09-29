
from abc import ABC,abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")

    def interest(self):
        pass

#sub class /child class of abstractclass
class SBI(bank):
    def interest(self):
        print("hello")

    def balance(self):
        print("balance in 300")

s=SBI()
s.bank_info()
s.balance()
s.interest()


from abc import ABC,abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest (self):
        "abstractmethod"
        pass

class SBI(bank):
    def balance(self):
        print("balance in 200")

class sub1(SBI):
    def interest (self):
        print("In SBI bank interest in 10 rupees")

s=sub1()
s.bank_info()
s.balance()
s.interest()


