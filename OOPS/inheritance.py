#inheritance

class Animal:
    name = ''
    age = ''
    def sleep(self):
        print(f"{self.name} will Sleep at night.")
    def Aging(self):
        print(f"{self.name} is {self.age} years old.")
    
class Dog(Animal):
    def __init__(self,name):
        self.name = name
    
d1 = Dog("Labradore")
d1.age = 10
d1.sleep()
d1.Aging()