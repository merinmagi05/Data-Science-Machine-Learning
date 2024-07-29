import numpy as np
arr=np.array([  [1+2j,4+3j,8+2j] ,
                [7+3j,2+3j,2+4j]  ], dtype=complex)
print("2D Array:")
print(arr)
#display no. of rows and columns
row,columns=arr.shape
print("\nNumber of rows:",row)
print("Number of columns:",columns)
dimensions=arr.ndim
print("Dimensions of array:",dimensions)
reshaped_array=arr.reshape(3, 2)
print("\nReshaped Array (3*2):")
print(reshaped_array)
