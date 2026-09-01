# add,subtr

import numpy as np

x = np.array([i for i in range(1,11)])

print(x)

print(x.reshape((2,5)))
# used to converting 1d to 2d

print(np.arange(9))

y = np.arange(1,9).reshape(2,4)

print(y)

print(y.ndim)

print(y.flatten())      # converting 2d/3d array into 1d array

a = np.array([[1,2,3,4],[5,6,7,8]])

b = np.array([[1,2,3,4],[5,6,7,8]])

print(a+b)

print(np.add(a,b))

print(np.subtract(a,b))

print(np.multiply(a,b))

print(np.divide(a,b))

print(np.square(a))

print(np.sqrt(a))

print(a * 2)

print(a ** 2)

print(a / 2)

print(np.sum(a))                #sum of all elements in the array

print(np.sum(a,axis = None))    #sum of all elements in the array

print(np.sum(a,axis = 1))       #sum of all elements in the array in rowwise

print(np.sum(a,axis = 0))        #sum of all elements in the array in columnwise

#Sorting in array
#Arrange the elements in ascending or descending order

print(np.sort(a))

print(np.sort(a,axis=0))        #column wise sort

print(np.sort(a,axis=1))

print(np.sort(a,axis=1)[0,::-1])

print(np.sort(a,axis=1)[:,::-1])

print(np.sort(a,axis=0)[::-1,:])

# we are using slicing techmique so need to give row index and column index

arr = np.arange(1,21).reshape(5,4)

print(arr)

"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
"""

# arr[row_start:row_stop:step,column_start:column_stop:step]

print(arr[1:3,1:3])

print(arr[2:4,1::])

arr_2 = np.array([4,3,5,7,2,10])

print(arr_2.argmax())               # returns the index of largest element

print(arr_2.argmin())               # returns the index of smallest element

print(arr_2.argsort())              # get the indices that produced the sorted order

c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(c.argmax())                   # 9 return the index after flatten the 2d array

print(c.argmax(axis=0))

print(c.argmax(axis=1))

# where
# np.where(condition)
# use to poitioning the elements which satisfy the condition
# replace the elements from the arrray those satisfy the condition

print(np.where(arr_2 > 5))

print(np.where(c > 5))        # 1st row 1st element, 1st row 2nd element

print(np.where(c > 5,"pass","fail"))

# np.where(condition,value_if_true,value_if_false)

arr1 = np.array([[30,10,90],
                [20,40,70],
                [25,45,80]])

print(arr1[0:2,0:2])

print(arr1[:,0:2])

print(arr1[0:2,:])

print(arr1[::-1,:])

print(arr1[:,::-1])

print(arr1[0:2,::-1])

print(arr1[::-1,::-1])

print(np.sort(arr1))

print(np.sort(arr1)[:,::-1])

print(np.sort(arr1)[::-1,::-1])

print(np.sort(arr1,axis=0))

print(np.sort(arr1,axis=0)[:,::-1])

print(np.sort(arr1,axis=0)[::-1,::-1])

arr2 = np.array([4.65,5.35,6.98,7.5])

print(np.floor(arr2))   # returns the largest iteger <= the number given

print(np.round(arr2))   # round the number to the nearest integer by default

print(np.ceil(arr2))    # return the smallest number >= the number given