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

print(zerod.ndim)
print(oned.ndim)
print(twod.ndim)
print(threed.ndim)
print(multid.ndim)
print("\n")
#CRUD operations on Numpy Arrays
#reading from a numpy array
sample_array = np.array([1,2,3,4,5,6,7,8,9,10])
for i in range(0,len(sample_array)):
    print(sample_array[i], end=" ")
print("\n")

#updating elements in a numpy array, using indexing
sample_array[9] = 100
print(sample_array)
print("\n")

#deleting elements from a numpy array
sample_array = np.delete(sample_array, 9)
print(sample_array)
print("\n")

#searching elements in a numpy array
x = list(range(0,20000, 5))
sample_search_array = np.array(x)
#searching for the element 5500
res = np.where(sample_search_array == 5500)
print(res)
#checking if the returning index is true
print(sample_search_array[1100])

#sorting elements in a numpy array
sample_sort_array = np.array([1,4,9,2,3,8,7,6])
#sorting the numpy array using the sort() function
x = np.sort(sample_sort_array)
print(x) 

#mathematical operations on numpy arrays
a = np.array([[1,2,3]], dtype = np.int64)
b = np.array([[4,5,6]], dtype = np.int64)
#addition
addition = np.add(a,b)
print(addition)
print("\n")
#subtraction
subtraction = np.subtract(a,b)
print(subtraction)
print("\n")
#multiplication
multiplication = np.multiply(a,b)
print(multiplication)
print("\n")
#division
division = np.divide(a,b)  
print(division)
print("\n")
#square root
sqrt = np.sqrt(a)  
sqrt2 = np.sqrt(b) 
print(sqrt)
print(sqrt2)
print("\n")
#transpose
x = np.array([[1,2,3],[1,2,3],[1,2,3]])
transpose = np.transpose(x)
print(x)
print("\n")
print(transpose)
print("\n")

