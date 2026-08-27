def fib_list(n) :
    fib_list = []
    a, b = 0, 1
    for i in range (n):
        fib_list.append(a)
        a, b = b, a + b

    return fib_list
print(fib_list(10))


def fib_gen(n) :
    a = 0
    b = 1
    for i in range (n) :
        yield a 
        a, b = b, a + b
        
print(list(fib_gen(10)))



def fib_list(n):
    fib_list = []
    a,b = 0,1
    for i in range (n) :
        fib_list.append(a)
        a , b = b , a + b
    return fib_list
print(fib_list(10))

def fib_gen(n):
    a,b = 0,1
    for i in range (n) :
        print ("before : " , a)
        yield a
        a , b = b , a + b 
print(list(fib_gen(10)))

x = fib_list(10)
y = fib_gen(10)
print(type(x))
print(type(y))

# First loop :
g = fib_gen(5)
print("First loop : ")
for num in g :
    print(num)
#Second loop :  
print("Second loop : ")
for num in g :
    print (num)