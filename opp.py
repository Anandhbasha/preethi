# car
# no_ofWheels = 4
# no_of_airbags = 5
# milage = 20
# color = "red"

# def movingForword():
#     print("Accelaror Pressed")

# def carStopes():
#     print("Break Appears")


# class Car:
#     no_ofWheels = 4
#     no_of_airbags = 5
#     milage = 20
#     color = "red"
#     def movingForword(self):
#         print("Accelaror Pressed")

#     def carStopes(self):
#         print("Break Appears")

# car1 = Car()


# car1.movingForword()
# car2 = Car()
# car2.milage= 30
# print("car2 Milage:", car2.milage)
# print("car1 Milage:",car1.milage)


# # encapsulation
# class Students:
#     __total_marks = 0
#     # private variable

#     def set_marks(self,mark):
#         if mark >=0 and mark <=100:
#             Students.__total_marks+=mark
#         else:
#             print("Invalid Mark")
#     def get_mark(self):
#         return Students.__total_marks
# s1 = Students()
# # s1.__total_marks=100
# s1.set_marks(90)
# print(s1.get_mark())

# abstraction
# from abc import ABC,abstractmethod
# class PaymentGateWay(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
# class Gpay(PaymentGateWay):
#     def pay(self, amount):
#         print(f'Paid {amount} via Gpay')
# class Phonepe(PaymentGateWay):
#     def pay(self, amount):
#         print(f'Paid {amount} via phonepe')

# # Gpay
# payment = Gpay()
# payment.pay(500)

# # Phonepe
# payPhonepe = Phonepe()
# payPhonepe.pay(6000)


# # inhertence
# class Vehicle:
#     def vehicle(self):
#         self._total_airbags = 5
#         print("The vehicle is startes")
# class Car(Vehicle):
#     def car(self):
#         print(self._total_airbags)
#         print("car is on")


# c = Car()
# c.vehicle()
# c.car()


# # polymorphism

# # method overloading
# class Calculator:
#     def add(self,a=0,b=0,c=0):
#         res = a+b+c
#         print(res)

# calc = Calculator()
# calc.add(10,5,6)
# calc.add(10,5)
# calc.add()

# # overWriting

class Resturant:
    def place_order(self):
        print("order Placed from General Res")
class VegResturant(Resturant):
    def place_order(self):
        print("order Placed from General VegResturant")
class NonVegResturant(Resturant):
    def place_order(self):
        print("order Placed from General NonVegResturant")


def order(res:Resturant):
    res.place_order()

order(NonVegResturant())
order(VegResturant())
order(Resturant())

# # # private variable
# # # __totalmarks
# # # protect
# # # _total marks


# # # Multiple
# # class A:
# #     pass
# # class B:
# #     pass
# # class C:
# #     pass
# # class d(A,B,C):
# #     pass

# class Camera:
#     def allowCam(self):
#         print("Allow access")
# class Phone:
#     def accesContact(self):
#         print("Allow contact")
# class Microphone:
#     def accessMick(self):
#         print("Allow mike")
# class Smartphone(Camera,Phone,Microphone):
#     def installApp(self):
#         print("App Installed")

# mobile = Smartphone()
# mobile.accessMick()
# mobile.allowCam()
# mobile.accesContact()
# mobile.installApp()



# # compostion
# class Doctor:
#     def __init__(self,name):
#         self.name = name
#     def treat(self):
#         print(f'Dr Name is{self.name}')
# class Patient:
#     def __init__(self,name):
#         self.name = name
#     def suffer(self):
#         print(f'Patient name is{self.name}')
# class Hospital:
#     def __init__(self,doctor,patient):
#         self.doctor = doctor
#         self.patient = patient
#     def treatment(self):
#         print("Treatment Starts in Hospital")
#         self.patient.suffer()
#         self.doctor.treat()

# doc = Doctor("xyz")
# pat1 = Patient("abc")


# hos1 = Hospital(doc,pat1)
# hos1.treatment()

# class A:
#     def hello(self):
#         print("Hello")


# s = A()
# s.hello()

# A.hello(s)

# # static method
# class Calc:
#     # @staticmethod
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
#     def mul(a,b):
#         return a*b

# print("Add:",Calc.add(10,5))
# print("Sub:",Calc.sub(10,5))
# print("mul:",Calc.mul(10,5))


# # cls method
# class Member:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Member.count+=1    
#     def total_members(cls):
#         print("Total Members :",cls.count)

# m = Member("abc")
# m1 = Member("xyz")

# Member.total_members()


# # without
# class Studnet:
#     def __init__(self,name,course,Fees):
#         self.name = name
#         self.course= course
#         self.Fees = Fees
# s1 = Studnet("xyz","Python","10000")
# s2 = Studnet("abc","Java","12000")

# withClass
# factory
# class Students:
#     def __init__(self,name,course,fees):
#         self.name = name
#         self.course= course
#         self.fees = fees
#     @classmethod
#     def create_python(cls,name):
#         return cls(name,"Python",10000)
#     @classmethod
#     def create_java(cls,name):
#         return cls(name,"Java",12000)


# stud1 = Students.create_python("abc")
# stud2 = Students.create_java("xyz")

# print(stud1.name,stud1.course,stud1.fees)
# print(stud2.name,stud2.course,stud2.fees)



'''
Module
'''
# from functions import number_to_words,num

# print(number_to_words(num))




def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(5, 10))
