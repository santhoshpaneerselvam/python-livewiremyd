from abc import ABC,abstractmethod
class college(ABC):
    def name(self):
        print("santhosh")
    @abstractmethod
    def interest(self):
        "abstractmethod"
        pass


class student(college):
    def group(self):
        print ("engineering")

class student2 (student):
    def interest(self):
        print ("B.tech")

k=student2()
k.name()
k.group()
k.interest()
