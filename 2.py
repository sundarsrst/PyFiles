def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False
a = dog_check("hey this is dog")
print(a)

def dog_checks(my_string):
    if 'dogy' in my_string:
        return True
    else:
        return False
b = dog_checks("hey this is dogyy")
print(b)

def pig_latin(word):
    first_letter = word[0]
    #check if a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word
a = pig_latin('apple')
b = pig_latin('banana')
print(a,b)

def simple_function():
    print('it is a simple function')
simple_function()

def simple_function2(sexs):
    return ("he is" +sexs)
x = simple_function2("male")
print(x)


def myfunc(a,b):
    #return 5%of the sum of a and b
    return sum((a,b)) * 0.05
displaysum = myfunc(40,60)
print(displaysum)

def myfunc2(*args):
    #return 5%of the sum of a and b
    return sum((args)) * 0.05
displaysum2 = myfunc2(40,60,100,200,300)
print(displaysum2)

def myfunc3(*args):
    for items in args:
        print(items)
aa = myfunc3(40,60,70,80,90)
print (aa)

def myfunc3(x,y):
    for items in args:
        print(items)
items = myfunc3.input('input the items value')

