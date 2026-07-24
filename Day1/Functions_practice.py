def greet(name = "Friend"):
    return "Hello!" + name

print(greet())
print(greet("chirag"))


def greet(name = "Friend"):
    return "Hello!" + name

def get_avg(num) :
    if len(num) == 0 :
        return None
    return sum(num) / len(num)

print(greet())
print(greet("chirag"))
marks = [75, 10, 85, 45, 16]
print("Average marks : " , get_avg(marks))
empty_list = []
print("Average of empty list : ", get_avg(empty_list))