nums = [1,2,3,4,5,6,7,8,9,10]
square_loop = []
for i in nums:
    if i % 2 != 0:
        square_loop.append(i**2)
print(square_loop)


def odd_square(nums):
    square_loop = []
    for i in nums:
        if i % 2 == 1:
            square_loop.append(i**2)
    return square_loop
nums = [1,2,3,4,5,6,7,8,9,10]
print(odd_square(nums))

names = ["chirag", "ashish", "ravi", "meera", "dev"]
def up_names(names):
    upper_names = []
    for name in names:
        upper_names.append(name.strip().upper())
    return upper_names
print(up_names(names))


