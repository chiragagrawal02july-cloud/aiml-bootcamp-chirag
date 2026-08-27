numbers = [1,2,3]
it = iter(numbers)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration :
    print("Error : StopIteration")

print ("\nUsing while loop")
it = iter(numbers)
while True :
    try :
        i = next(it)
        print(i)
    except StopIteration :
        break

print("\nUsing For loop")
for i in numbers :
    print(i)