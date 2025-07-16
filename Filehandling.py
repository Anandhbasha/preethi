# # #read
# # file = open("new.txt",'r')
# # # print(file.read())
# # # file.close()

# # # readline
# # newLine = open("new.txt",'r')
# # # lines = (newLine.readlines())
# # line = (newLine.readline())
# # # print(lines)
# # print(line)
# # newLine.close()

# # #write 
# # # wri = open("new.txt",'w')
# # # wri.write("This new Written File")
# # # wri.close()

# # # write line
# # wri = open("new.txt",'w')
# # wriLines = ["This writeLines \n","This is Second operation of Txt File"]
# # # wriLine = "This writeLines"
# # wri.writelines(wriLines)
# # wri.close()

# # # append
# # append = open("new.txt",'a')
# # append.write("\n Add this at bottom")
# # print("Append is Done")
# # append.close()

# # with open("new.txt",'r') as f:
# #     print(f.read())

# # OS
# import os

# if os.path.exists("abc.txt"):
#     print("File Found")
# else:
#     print("File not found")

# # remove
# if os.path.exists("new.txt"):
#     os.remove("new.txt")
# # seek
# # tell
with open("py.txt",'r') as file:
    print(file.tell())
    print(file.seek(6))
    print(file.tell())
    print(file.read())


# Reverse
# userInput = input("Enter the Value")
# userInput[0] = 1
# userInput[1] = 0
# print(userInput[-2])
# len(userInput)-1 = 2-1 = 1
# reversed =""
# for i in range(len(userInput)-1,-1,-1):
#     reversed+=userInput[i]
# print(reversed)

# Armstrong
# # 153-> 1**3+5**3+3**3 = 153
# userInput1 = input("Enter the Value")
# total=0
# for nums in userInput1:
#     total+=int(nums)**3
# if total==int(userInput1):
#     print("Is Armstrong")
# else:
#     print("Not a Armstrong")

# Pyramid pattern
# rows = int(input("Enter Star"))
# for i in range(1,rows+1):
#     space = " " * (rows-1)
#     star = "*" * (2*i-1)
#     print(space+star)
    # print(""*(rows-1)+"*"*(2*i-1))


# n = int(input("Enter Star"))
# # get input

# for i in range(n):
#     # i=1
#     # i=2
#     for j in range(n-i-1):
#         # j=1   
#         # j=2
#         # j=3


#         # second time
#         # j = 1
#         # j=2
#         # j=3
#         # j=4
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()

# nested for loop
# for i in range(6):
#     print(i)
#     # i=0
#     # i=1
#     # i=2
#     # i=3
#     # 
#     for j in range(i-1,10):
#         # j = 0
#         # j=1
#         # j=2
#         # j=3
#         # j=4
#         # j=5
#         # j=6
#         # j=7
#         # j=8
#         # j=9
#         print(j)
