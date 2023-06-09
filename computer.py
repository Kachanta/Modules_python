class Computer:
    
    def __init__(self):
        self.name = "Reuben"
        self.age = 30
    
    def update(self, new_age):
        self.age = new_age
        
    def newname(self, new_name):
        self.name = new_name
        
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        
c1 = Computer()
c2 = Computer()

c1.update(40)
c2.update(90)

c1.newname("Johna")

if c2.compare(c1):
    print("thesame they are")
else:
    print("not thesame")
    
print(c1.name, c1.age)
print(c2.name, c2.age)