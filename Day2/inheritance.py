class Person :
    def __init__(self,name) :
        self.name = name
    def greet(self):
        print (f"Hello! My name is {self.name}.")

class Student (Person) :
    def __init__ (self, name, roll) :
        super().__init__(name)
        self.roll = roll
    def greet(self):
        print (f"Hello! I am student {self.name}. My roll no. is {self.roll}.")

class Teacher (Person) :
    def __init__ (self, name, subject) :
        super().__init__(name)
        self.subject = subject
    def show_subject(self):
        print(f"I teach {self.subject}.")

p1 = Person ("Ramesh")
s1 = Student ("Chirag" , 15)
t1 = Teacher ("Rakesh", "Python")

p1.greet()
print()
s1.greet()
print()
t1.greet()
t1.show_subject()