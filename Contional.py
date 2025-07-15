# # condtional Statements
#     # simple
# # age=17
# # # if age >=18:
# # #     print("Eligible to vote")
# # # if else
# # if age>=18:
# #     print("Eligible to vote")
# # else:
# #     print("Not Eligible")

# # salary = int(input("Enter Your salary"))
# # if salary>90000:
# #     print("He is high payable Employee")
# # elif salary>=80000:
# #     print("Something")
# # elif salary>=70000:
# #     print("Salary is Above 70k")
# # else:
# #     print("Basic Pay")

# # 


# # if UG>70 and HSC>70 and SSLC>70:
# #     print("He is Eligible for interview")
# # else:
# #     print("Not Eligible")



# UG = 60
# HSC = 70
# SSLC= 72

# if UG>70:
#     if HSC>70:
#         if SSLC >70:
#             print("Eligible")
#         else:
#             print("Because of SSLC")
#     else:
#         print("Because of HSC")
# else:
#     print("Because of UG")

# # ternary
# number = int(input("Enter the number to find Odd or Even"))
# print("Even" if number%2==0 else "Odd")

# # and or Not 
# age = 20
# nationailty = "India"
# if age >=18 or nationailty=="India":
#     print("Eligible")

# looping Statements
# while
# seconds = 5
# while seconds>0:
#     print(f'Time left:{seconds}')
#     # seconds = 5
#     seconds-=1
    # sec = 4
    # 3
    # 2
    # 1

# arr = [44,21,80,99,77]
# # print(arr[0])
# a=2
# while a<len(arr):
#     print(arr[a])
#     a+=1
# for
# for i in range(1,6):
#     print(i)

# fruits = ["apple","banana","cherry"]
# fruitName = str(input("Enter the Fruit Name: ")).lower()

# for fruit in fruits:
#     if fruitName==fruit:
#         print(f'You are selected: {fruit}')
#     else:
#         print("Invalid")

# numbers=[10,20,30]
# for num in numbers:
#     print(num*2)

# square = [a*a for a in range(1,11)]
# print(square)

# even = [e for e in square if e%2==0]
# print(even)

prices = [420,318,110]
finalPrice = [p+(p*0.18) for p in prices]
print(finalPrice)