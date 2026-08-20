import numpy as np

arr = np.array([1,2,3,4])

print(arr)

print(arr.ndim)

print(arr.shape)

# array contains a single row of elements it can be termed as 1-dimensional array

arr_2 = np.array([[1,2,3,4],[5,6,7,8]])

print(arr_2)

print(arr_2.ndim)

print(arr_2.shape)

# array contains 2 row of elements (rows and columns) a table like structure
# can be termed as 2-dimensional array

arr_3 = np.array([

            [[1,2,3,4],[5,6,7,8]],
            [[1,2,3,4],[5,6,7,8]],
            [[1,2,3,4],[5,6,7,8]]
                ])

print(arr_3)

print(arr_3.ndim)

print(arr_3.shape)
# 3d array
# An array contains more tham one 2d array can be termed as 3d array

"""
Types of matrix
"""
# Zero martrix : Matrix having all the elements as zero

m_1 = np.zeros((3,4),dtype=int)  #default is float , zero matrix having 3 rows and 4 columns with integer datatype

print(m_1)

# Ones matrix (matrix having all elements as 1)

m_2 = np.ones((4,3),dtype=int)

print(m_2)

# full matrix
# np.full(shape,value,dtype)

print(np.full((3,4),5,dtype=int))

# Identity matrix(rows and colums should be equal)

print(np.identity(n=3,dtype=int))

# or

print(np.eye(N=4,dtype=int))