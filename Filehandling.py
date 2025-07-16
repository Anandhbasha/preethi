# #read
# file = open("new.txt",'r')
# # print(file.read())
# # file.close()

# # readline
# newLine = open("new.txt",'r')
# # lines = (newLine.readlines())
# line = (newLine.readline())
# # print(lines)
# print(line)
# newLine.close()

# #write 
# # wri = open("new.txt",'w')
# # wri.write("This new Written File")
# # wri.close()

# # write line
# wri = open("new.txt",'w')
# wriLines = ["This writeLines \n","This is Second operation of Txt File"]
# # wriLine = "This writeLines"
# wri.writelines(wriLines)
# wri.close()

# # append
# append = open("new.txt",'a')
# append.write("\n Add this at bottom")
# print("Append is Done")
# append.close()

# with open("new.txt",'r') as f:
#     print(f.read())

# OS
import os

if os.path.exists("abc.txt"):
    print("File Found")
else:
    print("File not found")

# remove
if os.path.exists("new.txt"):
    os.remove("new.txt")
# seek
with open("py.txt",'r') as file:
    print(file.tell())
    print(file.seek(10))
# tell