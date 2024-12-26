class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Grade: ",self.grade)
    def walk(self):
        print(f"{self.name} can walk")
        print("Walking speed: ", (self.age*0.5+4))

s1 = Student("Jeeban", 20, "A")
s1.display()
s1.walk()

s2 = Student("Pooja", 16, "O")
s2.walk()