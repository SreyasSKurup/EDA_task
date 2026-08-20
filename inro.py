"""
EDA(exploratory data analysis)
Used to analyze the data  from different datasets using 4 different python libraries

numpy,pandas,matplotlib,seaborn

jupyter notebook
google collab

"""

"""
#
EDA (Exploratory data analysis)
EDA is the analysing the different datasets to understand its pattern
which can be termed as datahandling,data manipulation etc...

We use 4 different libraries
numpy,pandas,matplotlib,seaborn
"""
"""
Identify the problem --> Collecting the data (dataset) --> pandas - Analyze the dataset - analyzing missing values,removing the noise,filling values --> numpy - get the analyzed data numerical format --> used to train the model (ML) --> Evaluation and deployment
"""
"""
numpy
numerical python >>> used to do numerical and mathematical operations

array (faster than python list)
Array can be considered as a collection of element
It is homogeneous (one datatype only)
Vector based calculation (no iteration as in list) (Matrix based)

"""

"""
Array is faster than list 

for in in [1,2,3,4]
[1 2 3 4] * 2

array is a collection used to have more than one values
array does not have iteration as in list
"""
# pip install numpy

import numpy as np

elements = np.array([1,2,3,4])

print(elements)

print(elements.ndim)

"""
Two dimensional array
Array with elements in multiple rows (table like format)
np.array([[row1],[row2]])
"""

elements_2 = np.array([[1,2,3,4],[5,6,7,8]])

#3d array (contains multiple 2 dimensional arrays)

elements_3 = np.array([
    [[1,2,3,4],[4,5,6]],
    [[1,2,3,4][4,5,6]]

]
)

#Attributes
print(elements_3.ndim)
print(elements_3.dtype)
print(elements_3.shape)