import numpy as np
A=np.array([[1,2,3,4,5,6,],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30]])
print("MATRIX A:")
print(A)
B=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print("MATRIX B:")
print(B)

sub_matrix=A[:3,:3]
print("SUB MATRTIX:")
print(sub_matrix)

result=np.dot(sub_matrix,B)
print("Matrix after multiplication with the sub matrix of A and matrix B")
print(result)

A[:3,:3]=result
print("Matrix A after the operation:")
print(A)