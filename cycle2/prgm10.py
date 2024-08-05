import numpy as np
matrix_size=3
matrix=np.random.randint(10,20, size=(matrix_size,matrix_size))
print("ORIGINAL MATRIX:")
print(matrix)
if np.linalg.matrix_rank(matrix)== matrix_size:
    inverse_matrix=np.linalg.inv(matrix)
    print("\nINVERSE MATRIX")
    print(inverse_matrix)
else:
    print("\n The Matrix is not invertable(its rank is less than the size.")
rank=np.linalg.matrix_rank(matrix)
print("\nRANK OF THE MATRIX",rank)
determinant=np.linalg.det(matrix)
print("\nDETERMINANT OF THE MATRIX:",determinant)
matrix_1D=matrix.flatten()
print("\nMATRIX AS 1D ARRAY:")
print(matrix_1D)
eigenvalues, eigenvectors=np.linalg.eig(matrix)
print("\nEIGENVALUES:")
print(eigenvalues)
print("\nEIGENVECTORS:")
print(eigenvectors)