# Python Array Module
import array as myarray

# Creating an Array
arr = myarray.array('i', [1, 2, 3])
arr1 = myarray.array('d', [1.0, 2.1, 2.4, 2.5, 2.6])
arr2 = myarray.array('u', ['a', 'b', 'c', 'd'])
# typecodes
print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)
# first look at the array
print(arr)
print(arr1)
print(arr2)

#printing the length of an array
print(len(arr))
print(len(arr1))
print(len(arr2))

for i in range(0,len(arr)):
    print(arr[i], end=" ")
print("\n")
for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
print("\n")
for i in range(0,len(arr2)):
    print(arr2[i], end=" ")
print("\n")

# Indexing
#Assessing Elements from an Array using index values
x = list(range(1,100, 2))
new_array = myarray.array('i', x)

#printing the array
for i in range(0, len(new_array)):
    print(new_array[i], end=" ")
print("\n")

#accessing the element at index "25"
print(new_array[27])

#Adding Elements in an Array
new_arr = myarray.array('i', [3,4,5,6,7,8,9,10])
for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")
print("\n")
#adding elements in the array
new_arr.insert(2, 50)
#new_arr.insert(0, 1)
#printing the new array
for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")
print("\n")
#using append
new_arr.append(15)
for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")
print("\n")
#updating elements in an array
new_array = myarray.array('i', [1,2,2,4,5])

#printing the array
for i in range(0, len(new_array)):
    print(new_array[i], end=" ")
print("\n")

#updating the array
new_array[4] = 30 #assigned new value to the element at index 2
for i in range(0, len(new_array)):
    print(new_array[i], end=" ")
print("\n")

#deleting elements in an array
new_array.pop(2)

for i in range(0, len(new_array)):
    print(new_array[i], end=" ")
print("\n")

#using the remove method
new_array.remove(2)
for i in range(0, len(new_array)):
    print(new_array[i], end=" ")
print("\n")

#Slicing an Array
x = list(range(0,100, 3))
arr = myarray.array('i', x)

#slicing operations
arr0 = arr[10:20]
for i in range(0, len(arr0)):
    print(arr0[i], end=" ")
print("\n")

#negative slicing
arr1 = arr[10:-20]
for i in range(0, len(arr1)):
    print(arr1[i], end=" ")
print("\n")

#reversing the order using slicing
arr2 = arr[::-1]
for i in range(0, len(arr2)):
    print(arr2[i], end=" ")
print("\n")

#searching operations in an array using index
x = list(range(0,1000000, 2))
search_array = myarray.array('i', x)

#print first 10 elements
for i in range(0, len(search_array[0:10])):
    print(search_array[i], end=" ")
print("\n")

#search the number 10002 in the array
index = search_array.index(10002)
res = search_array[index]
print(index,res)

#sorting operations
sort_array = myarray.array('i', [5,3,4,6,9,7,8])
sorted_array = sort_array.tolist()

#ascending order
sorted_array.sort()
print(sorted_array)

#descending order
sorted_array.sort(reverse=True)
print(sorted_array)
