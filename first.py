a = 10 
b = -25 
print(type (a))
a = 10
b = 20
sum = a + b
print(sum)
Price = 99.95
pi = 3.14
print (type(Price))
print (type (pi))
print ("hello chirag")

try:
    name = chirag
except Exception as e:
    print(str(e))
name = 'chirag'
print(type(name))
is_student = True
is_logged_in = False
print(type(is_student))
chirag_is = True
chirag_are = False
print(type(chirag_is))
name = "chirag", "vaibhav", "sanjeev"
print(name)
print(type(name))
car = "bmw", "scorpio"
print(car)
print(type(car))
fruits = "orange", "banana"
print(fruits)
print (type(fruits))
student = {'name' : "Chirag",
        "age" : '24',
         "City" : 'Jaipur'
}
print(student)
a = [1,2,3]
b=a
b.append(4)
print(a)
print(b)
names = ['asha', 'meera', 'ravi', 'asha', 'ravi']
unique = []
for n in names :
    if n not in unique :
        unique.append(n)
print(unique)
for n in range (1,101) :
    if n % 3 == 0 and n % 5 == 0 : 
        print("FizzBuzz")
    if n % 3 == 0 : 
        print("Fizz")
    if n % 5 == 0 : 
        print("Buzz")
    else : 
        print(n)
result = []
for n in range (1,101) : 
    if n % 3 == 0 and n % 5 == 0 : 
        result.append("FizzBuzz")
    elif n % 3 == 0 : 
        result.append("Fizz")
    elif n % 5 == 0 :
        result.append("Buzz")
    else :
        print(result)
number = int(8)
if n % 2 == 0 :
    print("even")
else :
    print("odd")
class student :
    def __init__ (self,name,roll):
        self.name = name
        self.roll = roll
        self.marks = []
name = "chirag"
Roll = 15
def __init__ (self,name,roll):
    self.name = "chirag"
    self.roll = 15
    self.marks = []
student = "chirag",15
__init__ ("chirag",15)