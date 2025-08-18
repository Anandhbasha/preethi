# Numpy array creation,indexing operation
# 1D array

import numpy as np

# arr1 = np.array([10,20,30,40])

# print(arr1)

# # 2D array
# arr2 = np.array([[1,2],[3,4]])

# print(arr2)

# user_input = input("Enter the value")

# num_list = user_input.split()

# num_list = [int(i) for i in num_list]

# arr = np.array(num_list)
# print(arr)


# 3d array
# arr3 = np.array([[2,4],[10,20],[8,7]])

# print(arr3)

# zeroarr = np.zeros((3,4))

# print(zeroarr)


# onearr = np.ones((2))
# print(onearr)

# diagonal = np.eye(3)

# print(diagonal)


# defRange = np.arange(0,12,2)
# print(defRange)

# equal interval
# equal = np.linspace(0,1,5)
# print(equal)


# indexing

# twodarry = np.random.rand(2)
# print(twodarry)

# arr = np.array([10,20,30,40,50,60])
# print(arr[0])
# print(arr[0:2])
array2 = np.array([[100,200,300],[80,90,77]])

# print(array2[1,2])
# print(array2)

# print(array2[:,1])

# print(array2[0:2, 1:0])

arr = np.array([10,20,30])
arr1 = np.array([50,60,70])
print(arr[arr>10])
print(arr+arr1)

# reshape

arr = np.arange(12)
res = arr.reshape(3,4)
print(res)

flat = res.flatten()
print(flat)
