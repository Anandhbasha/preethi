# def greet():
#     print("Welcome to Functions")
# greet()

# # positional Argument
# # def add(num1,num2):
# #     print(num1+num2)

# # add(60,80)
# # add(80,70)
# # add(55,70)
# # default arguments function
# def add(num1=10,num2=50):
#     print(num1+num2)

# add()
# add(88,90)

# # keyword Arguments
# def user(name,age):
#     print(name,age)
# user(age=21,name="xyz")

# def multiple(a,b):
#     return a*b
# print(multiple(5,2))
# print(10)

# def calling():
#     return "Hello"

# newcall = calling()
# print(newcall)

# # variable iength arguments
# def show(*names):
#     for name in names:
#         print (name)
# show("xyz","abc","def")


# # anonyums function
# # lambda

# # square = lambda x:x*x
# # print(square(2))


# # scope
# # local scope
# # def square(x):
# #     d=50
# #     print(d)
# #     print(x*x)
# # print(d)

# # global scope
# d=50
# def square(x):
#     d=50
#     print(d)
#     print(x*x)
# print(d)
# square(5)

# n = int(input("Enter number of rows: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         # 1
#         # 1,2
#         # 1,2,3
#         # 1,2,3,4
#         print(j, end=' ')
#     print()

# arr = [1,2,3,4,5]
# k=3
# n=len(arr)
# rotated = []
# # 4
# # 5
# # 1
# # 2
# # 3
# for i in range(k,n):
#     rotated.append(arr[i])

# for x in range(0,k):
#     rotated.append(arr[x])

# print(rotated)

# arr = [1,2,1,3,3]
# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num] +=1
#     else:
#         freq[num] = 1
# for key in freq:
#     print(f'{key}=>{freq[key]} times')

# Zero = [1, 0, 4, 8, 0, 2] 
# res = []
# for x in Zero:
#     if x!=0:
#         res.append(x)

# # [1,4,8,2]

# zero_count = Zero.count(0)
# res.extend([0]* zero_count)
# print(res)

lar = [10,25,22,44,65]
second = float('-inf')
largest = second

for n in lar:
    if n > largest:
        second=lar
        lar = n
    elif n >second and n!=lar:
        second = n
print(second)


def number_to_words(num):
    words = ["Zero","One","Two","Three","Five","Six","Seven","Eight","Nine"]
    result =[]
    "123"
    # 1
    for digit in str(num):
        result.append(words[int(digit)])
        # 1
        # words[1] = "One"
    return " ".join(result)
num = 123
print(number_to_words(num))