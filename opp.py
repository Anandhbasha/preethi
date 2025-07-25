# class Blueprint of Object
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)


S=Student("Xyz",25)
S.show()

# Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance=1000
    def deposit(self,amount):
        # amount = 5000
        self.__balance+=amount
        # self.balance=6000
    def getBalance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(5000)
print(acc.getBalance())

# inheritance
class Animal:
    def speak(self):
        print("Animal Speaks")
class Dog(Animal):
    def bark(self):
        print("Dog Barks")

d= Dog()
d.speak()
d.bark()

# polymorphism
class Bird:
    def fly(self):
        print("Bird Flies")
class aeroplane:
    def fly(self):
        print("Aeroplane Flies")

def lifting(obj):
    obj.fly()

lifting(Bird())
lifting(aeroplane())

