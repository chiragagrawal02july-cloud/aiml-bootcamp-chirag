class Student : 
    def __init__ (self, name, roll) :
        self.name = name
        self.roll = roll
        self.marks = []

    def add_marks (self,score) :
        self.marks.append(score)

    def get_avg(self):
        if len(self.marks) == 0 :
            return 0
        return sum(self.marks)/len(self.marks)

    def highest(self) :
        if len(self.marks) == 0 :
            return None
        return max(self.marks)

    def lowest(self) :
        if len(self.marks) == 0 :
            return None
        return min(self.marks)


s1 = Student ('chirag', 15)
s1.add_marks (80)
s1.add_marks (90)
s1.add_marks (70)

s2 = Student ('rahul', 25)
s2.add_marks (50)
s2.add_marks (45)
s2.add_marks (67)

s3 = Student ('asha', 5)
s3.add_marks (65)
s3.add_marks (75)
s3.add_marks (84)

print("Student : ", s1.name)
print("roll : ", s1.roll)
print("marks : ", s1.marks)
print("avg score : ", s1.get_avg())
print("highest : ", s1.highest())
print("lowest : ", s1.lowest())

print("Student : ", s2.name)
print("roll : ", s2.roll)
print("marks : ", s2.marks)
print("avg score : ", s2.get_avg())
print("highest : ", s2.highest())
print("lowest : ", s2.lowest())

print("Student : ", s3.name)
print("roll : ", s3.roll)
print("marks : ", s3.marks)
print("avg score : ", s3.get_avg())
print("highest : ", s3.highest())
print("lowest : ", s3.lowest())