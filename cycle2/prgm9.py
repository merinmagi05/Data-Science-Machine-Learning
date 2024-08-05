import numpy as np
arr=np.array([1,2,3,4,5])
diagonal_matrix=np.diag(arr)
print("1D ARRAY:")
print(arr)
print("\n DIAGONAL MATRIX:")
print(diagonal_matrix)
arr2D_square=np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])
diagonal_elements=np.diag(arr2D_square)
print("\n2D SQUARE MATRIX:")
print(arr2D_square)
print("\nDIAGONAL ELEMENTS:")
print(diagonal_elements)
arr2D_non_square=np.array([[1,2,3],
                       [4,5,6]])
diagonal_elements_nonsquare=np.diag(arr2D_non_square)
print("\n2D NON-SQUARE MATRIX")
print(arr2D_non_square)
print("\nDIAGONAL ELEMENTS (NON-SQUARE)")
print(diagonal_elements_nonsquare)