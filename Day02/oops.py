class Student :
    def __init__ (self, name, roll) :
        self.name = name
        self.roll = roll
        self.marks = []

    def add_marks (self, score):
        self.marks.append(score)

    def get_avg(self):
        if len(self.marks) == 0 :
            return 0
        return sum(self.marks)/len(self.marks)

    def highest(self):
        if len(self.marks) == 0 :
            return None
        return max(self.marks)

    def lowest(self):
        if len(self.marks) == 0 :
            return None
        return min(self.marks)

        pass

s1 = Student ('chirag', 17)
s1.add_marks (54)
s1.add_marks (64)
s1.add_marks (100)

print("Student : ", s1.name)
print("roll : ", s1.roll)
print("marks : ", s1.marks)
print("avg score : ", s1.get_avg())
print("highest : ", s1.highest())
print("lowest : ", s1.lowest())