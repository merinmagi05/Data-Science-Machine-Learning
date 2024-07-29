import numpy as np
matrix1=np.array([
    [2,4,5],
    [6,12,8],
    [8,4,23]
])
matrix2=np.array([
    [4,5,2],
    [3,3,1],
    [1,8,2]
])
matrix_add=matrix1 + matrix2
matrix_diff=matrix1 - matrix2
matrix_div=matrix1 / matrix2
matrix_product=matrix1 * matrix2
matrix_mul=np.dot(matrix1, matrix2)
matrix_trans=np.transpose(matrix1)
matrix_diagonal_sum=np.trace(matrix1)
print("Matrix1:\n",matrix1)
print("Matrix2:\n",matrix2)
print("a.Matrix sum:\n",matrix_add)
print("b.Matrix Difference:\n",matrix_diff)
print("c.Matrix element-wise Product:\n",matrix_product)
print("d.Matrix element-wise Division:\n",matrix_div)
print("e.Matrix Multiplication:\n",matrix_mul)
print("f.Transpose of a matrix:\n",matrix_trans)
print("g.Sum of diagonal elements of the matrix:\n",matrix_diagonal_sum)