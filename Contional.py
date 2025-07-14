# condtional Statements
    # simple
# age=17
# # if age >=18:
# #     print("Eligible to vote")
# # if else
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible")

# salary = int(input("Enter Your salary"))
# if salary>90000:
#     print("He is high payable Employee")
# elif salary>=80000:
#     print("Something")
# elif salary>=70000:
#     print("Salary is Above 70k")
# else:
#     print("Basic Pay")

# 


# if UG>70 and HSC>70 and SSLC>70:
#     print("He is Eligible for interview")
# else:
#     print("Not Eligible")



UG = 60
HSC = 70
SSLC= 72

if UG>70:
    if HSC>70:
        if SSLC >70:
            print("Eligible")
        else:
            print("Because of SSLC")
    else:
        print("Because of HSC")
else:
    print("Because of UG")

# ternary
number = int(input("Enter the number to find Odd or Even"))
print("Even" if number%2==0 else "Odd")

# and or Not 
age = 20
nationailty = "India"
if age >=18 or nationailty=="India":
    print("Eligible")