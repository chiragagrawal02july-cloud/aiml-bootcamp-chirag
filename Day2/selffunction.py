class Student : 
    def __init__ (self, name, roll) :
        self.name = name
        self.roll = roll
    def __str__ (self) :
        return f"Student name : {self.name} , Roll no. : {self.roll}"
    def __repr__(self) :
        return f"Student('{self.name}' , {self.roll})"


s1 = Student ("Chirag", 15)

print("printing Student : ")
print(s1)
print()
students = [s1]
print("printing list : ")
print(students)