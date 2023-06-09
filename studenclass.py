class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self):
        return self.m1 + self.m2
    
    def avg(self):
        return (self.m1 + self.m2)/2
    
    def __add__(self, other):
        s1 = self.m1 + self.m2
        other = self.m1 + self.m2
        return s1 + other
        
s1 = Student(50,43)
s2 = Student(98, 23)

print(s1.sum())
print(s1.avg())
print(s1+s2)
print(s1.__add__(s2))
print(Student.__add__(self, other))