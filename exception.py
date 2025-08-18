# Syntax Error
# #  if True
# # print("Hello")

# # Tab error
# for i in range(3):
#     print(i)

# # not defined
# # print(a)

# a=10
# def test():
#     print(a)
#     a+=1
# test()

# num = 5+"10"

# # valueError
# userInput = int("abc")

# overflowError
# import math
# print(math.exp(10000))

# zerodivision Error
# print(5/0)

# index error
# nums = [1,2,3,4]
# print(nums[5])

# key value
# data = {"name":"xyz"}
# print(data[age])

# # Filenot Found error
# with open("new.pdf") as f:
#     print(f)

# try:
#     num = int(input("Enter the number to add"))
#     print(5/num)
# except ValueError:
#     print("Please the Number to do Division")
# except ZeroDivisionError:
#     print("Dont use Zero")

# # try-Except-else
# try:
#     num = int(input("Enter the number to add"))    
# except ValueError:
#     print("Please the Number to do Division")
# else:
#     print(5/num)
# finally:
#     print("This work is Completed")

class NegativenumError(Exception):
    pass
try:
    age = int(input("Enter Postive Number"))
    if age < 18:
        raise NegativenumError("Not Eligible")
    print("Number Accepted",age)
except NegativenumError as e:
    print("Custom Error",e)



# numpy
# pandas
# GUI
# widget