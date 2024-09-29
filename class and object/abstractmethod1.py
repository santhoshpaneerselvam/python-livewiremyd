
from abc import ABC,abstractmethod

class bank(ABC):
    def bank_info(self):
        print("weloome to bank")
    @abstractmethod
    def interest (self):
        pass

#sub class /child class of abstract class
class SBI(bank):
    def interest(self):
        print("5 percentage")


s=SBI()
s.bank_info()
s.interest()

