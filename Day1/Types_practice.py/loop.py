#For loop way
name = ["asha", "ravi", "asha", "meera", "ravi"]
unique = []
for el in name :
    if el not in unique :
        unique.append(el)
    else :
        pass
print(unique)


names = ["asha", "ravi", "asha", "meera", "ravi"]
name_length = {}
for name in names:
    name_length[name] = len(name)
print(name_length)



for i in range (1,101) :
    if i % 3 == 0 and i % 5 == 0 :
        print ("FizzBuzz")
    elif i % 3 == 0 :
        print ("Fizz")
    elif i % 5 == 0 :
        print ("Buzz")
    else :
        print (i)




result = []
for i in range (1,101) :
    if i % 3 == 0 and i % 5 == 0 :
        result.append("FizzBuzz")
    elif i % 3 == 0 :
        result.append("Fizz")
    elif i % 5 == 0 :
        result.append("Buzz")
    else :
        result.append(i)
print(result)



def fizzbuzz(limit, div1, word1, div2, word2):
    result = []
    
    for i in range (1, limit +1):
        text = ""
        if i % div1 == 0 :
            text += word1
        if i % div2 == 0 :
            text += word2
        if text == "" :
            text = str(i)
            
        result.append(text)
    
    return result

print (fizzbuzz(100,2,"EVEN",7,"bye"))

