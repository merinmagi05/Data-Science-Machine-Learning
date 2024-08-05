import numpy as np
array1D=([1,2,3,4,5])
print("\n\n1D ARRAY BEFORE INSERTION:")
print(array1D)
array1D=np.insert(array1D,2,6)
print("ARRAY AFTER INSERTION:")
print(array1D)
array2D=np.array([
                [1,2,3],
                [4,5,6]  ])
print("2D ARRAY:")
print(array2D)
array2D=np.insert(array2D,1,[7,8,9],axis=0)
print("\n2D ARRAY AFTER INSERTION:")
print(array2D)