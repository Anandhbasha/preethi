def greet():
    print("Welcome to Functions")
greet()

# positional Argument
# def add(num1,num2):
#     print(num1+num2)

# add(60,80)
# add(80,70)
# add(55,70)
# default arguments function
def add(num1=10,num2=50):
    print(num1+num2)

add()
add(88,90)

# keyword Arguments
def user(name,age):
    print(name,age)
user(age=21,name="xyz")

def multiple(a,b):
    return a*b
print(multiple(5,2))
print(10)

def calling():
    return "Hello"

newcall = calling()
print(newcall)

# variable iength arguments
def show(*names):
    for name in names:
        print (name)
show("xyz","abc","def")


# anonyums function
# lambda

# square = lambda x:x*x
# print(square(2))


# scope
# local scope
# def square(x):
#     d=50
#     print(d)
#     print(x*x)
# print(d)

# global scope
d=50
def square(x):
    d=50
    print(d)
    print(x*x)
print(d)
square(5)

