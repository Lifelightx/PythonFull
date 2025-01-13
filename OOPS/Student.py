class Student:
    collegeName = "Institute of Management and Information Technology"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avgMarks(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum/3
    
    

s1 = Student('Jeeban', [89,87,67])
x = s1.avgMarks()
print(x)
print(s1.collegeName)

s2 = Student('Pooja', [67,89,76])
print(s2.avgMarks())
print(s2.collegeName)
