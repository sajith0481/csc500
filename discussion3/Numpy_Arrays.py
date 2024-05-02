import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("\n")


#creating an array with all zeros
zeros = np.zeros((2,2))
#creating an array with all ones
ones = np.ones((2,2))
#creating an array with constant values
const = np.full((3,3), 5)
#creating an identity matrix
iden = np.eye(2)
#creating a random matrix
rand = np.random.random((2,2))

print(zeros)
print("\n")
print(ones)
print("\n")
print(const)
print("\n")
print(iden)
print("\n")
print(rand)
print("\n")

#0-dimensional array
zerod = np.array(1)
print(zerod)    
print("\n")
#1-dimensional array
oned = np.array([1,1])
print(oned)
print("\n")
#2-dimensional array
twod = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(twod)
print("\n")
#3-dimensional array
threed = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(threed)
print("\n")
#multi-dimensional array
multid = np.array([1,2,3,4,5], ndmin=5)
print(multid)
print("\n")
