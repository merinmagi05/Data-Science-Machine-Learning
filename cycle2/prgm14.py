
import numpy as np
A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[9,8,7],
            [6,5,4],
            [3,2,1]])
C=np.array([[10,5,9],
            [20,15,19],
            [30,2,29]])
result=np.dot(np.dot(A,B+),C)
print("MATRIX A:")
print(A)
print("MATRIX B:")
print(B)
print("MATRIX C:")
print(C)
print("Result of (A*B)*C:")
print(result)