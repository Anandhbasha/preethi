# # # car
# # no_ofWheels = 4
# # no_of_airbags = 5
# # milage = 20
# # color = "red"

# # def movingForword():
# #     print("Accelaror Pressed")

# # def carStopes():
# #     print("Break Appears")


# class car:
#     no_ofWheels = 4
#     no_of_airbags = 5
#     milage = 20
#     color = "red"
#     def movingForword(self):
#         print("Accelaror Pressed")

#     def carStopes(self):
#         print("Break Appears")

# car1 = car()


# car1.movingForword()
# car2 = car()
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
# s1.set_marks(80)
# print(s1.get_mark())

# # abstraction
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
#         self._total_marks = 100
#         print("The vehicle is startes")
# class Car(Vehicle):
#     def car(self):
#         print(self._total_marks)
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

# class Resturant:
#     def place_order(self):
#         print("order Placed from General Res")
# class VegResturant(Resturant):
#     def place_order(self):
#         print("order Placed from General VegResturant")
# class NonVegResturant(Resturant):
#     def place_order(self):
#         print("order Placed from General NonVegResturant")


# def order(res:Resturant):
#     res.place_order()

# order(NonVegResturant())
# order(VegResturant())
# order(Resturant())

# # private variable
# # __totalmarks
# # protect
# # _total marks


# # Multiple
# class A:
#     pass
# class B:
#     pass
# class C:
#     pass
# class d(A,B,C):
#     pass

class Camera:
    def allowCam(self):
        print("Allow access")
class Phone:
    def accesContact(self):
        print("Allow contact")
class Microphone:
    def accessMick(self):
        print("Allow mike")
class Smartphone(Camera,Phone,Microphone):
    def installApp(self):
        print("App Installed")

mobile = Smartphone()
mobile.accessMick()
mobile.allowCam()
mobile.accesContact()
mobile.installApp()



# compostion
class Doctor:
    def __init__(self,name):
        self.name = name
    def treat(self):
        print(f'Dr Name is{self.name}')
class Patient:
    def __init__(self,name):
        self.name = name
    def suffer(self):
        print(f'Patient name is{self.name}')
class Hospital:
    def __init__(self,doctor,patient):
        self.doctor = doctor
        self.patient = patient
    def treatment(self):
        print("Treatment Starts in Hospital")
        self.patient.suffer()
        self.doctor.treat()

doc = Doctor("xyz")
pat1 = Patient("abc")


hos1 = Hospital(doc,pat1)
hos1.treatment()

