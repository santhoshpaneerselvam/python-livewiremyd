
from abc import ABC,abstractmethod
class school(ABC):
    def school_rules(self):
        print("assemble the prayer")
    @abstractmethod
    def interest(self):
        "abstractmethod"
        pass

#child class  of abstract class
class parent(school):
    def child(self):
        print ("school admission")

class child1 (parent):
    def interest(self):
        print ("In school admission interest in your child")


k=child1()
k.school_rules()
k.child()
k.interest()
