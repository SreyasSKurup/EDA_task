import numpy as np

arr = np.array([
[10, 25, 30, 45],
[15, 20, 35, 40],
[50, 60, 55, 70],
[80, 75, 90, 65]
])

# 1. Display the array. (print(arr))
print(arr)

# 2. Find the number of dimensions. (arr.ndim) 
print(arr.ndim)

# 3. Find the shape of the array. (arr.shape)
print(arr.shape)

# 4. Find the total number of elements. (arr.size)
print(arr.size)

# 5. Find the data type of the array. (arr.dtype)
print(arr.dtype)

# 6. Print the element at row 2, column 3. Expected value: 35. (Use 0-based indexing.)
print(arr[1,2])

# 7. Print the first row. Expected: [10 25 30 45]. (Use indexing.)
print(arr[0])

# 8. Print the last row. Expected: [80 75 90 65]. (Use indexing.)
print(arr[-1])

# 9. Print the first column. Expected: [10 15 50 80]. (Use slicing.)
print(arr[:,0])

# 10. Extract the 2 × 2 sub-array [[25, 30], [20, 35]]. (Use 2D slicing.)
print(arr[0:2, 1:3])

# 11. Find the sum of all elements
print(np.sum(arr))

# 12. Find the maximum value
print(np.max(arr))

# 13. Find the minimum value
print(np.min(arr))

# 14. Find the mean of all elements
print(np.mean(arr))

# 15. Find the sum of each row
print(np.sum(arr, axis=1))

# 16. Find the sum of each column
print(np.sum(arr, axis=0))

# 17. Find the index of the maximum value
print(np.argmax(arr))

# Find maximum index for each row
print(np.argmax(arr, axis=1))

# 18. Find the index of the minimum value. (np.argmin(arr) and try np.argmin(arr, axis=0))
print(np.argmin(arr))

# Find minimum index for each column
print(np.argmin(arr, axis=0))

# 19. Sort the array row-wise in ascending order
print(np.sort(arr, axis=1))

# 20. Find the sorting indexes row-wise
print(np.argsort(arr, axis=1))

