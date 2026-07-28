names = ["chirag", "ashish", "ravi", "meera", "aasha"]
marks = [88, 92, 79, 40, 35]
result = zip(names, marks)
print(list(result))

def combine_lists(names, marks):
    result = []
    for i in range(len(names)):
        result.append((names[i], marks[i]))
    return result

names = ["chirag", "ashish", "ravi", "meera", "aasha"]
marks = [88, 92, 79, 40, 35]
print(combine_lists(names,marks))

def combine_lists(names, marks):
    result = []
    for a, b in zip(names, marks) :
        result.append((a, b))
    return result
names = ["chirag", "ashish", "ravi", "meera", "aasha"]
marks = [88, 92, 79, 40, 35]
print(combine_lists(names,marks))


def productive_list(list1, list2) :
    result = []
    for a, b in zip (list1, list2):
        result.append(a*b)
    return result
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print(productive_list(list1, list2))