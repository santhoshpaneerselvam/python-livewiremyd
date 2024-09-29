
from abc import ABC,abstractmethod
class bank (ABC):
    def bank_info(self):
        print ("welcome to bank")
    def interest(self):
        "abstract means"
        pass


class SBI (bank):
    def balance (self):
        print ("balance in 200")


class subi(SBI):
    def interest(self):
        print ("In SBI bank interest in 7 rupees")


s=subi()
s.bank_info()
s.balance()
s.interest()

