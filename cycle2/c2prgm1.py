import numpy as np

# 3D array = 2 planes * 3 rows * 4 columns
arr = np.array([
    [[1.5, 2.1, 3.4, 2.3], [3.4, 2.0, 5.3, 4.6], [1.2, 3.2, 1.0, 3.0]],  # Plane 1
    [[2.7, 4.2, 8.2, 4.6], [9.3, 2.0, 4.0, 5.0], [4.0, 1.0, 2.0, 4.3]]   # Plane 2
], dtype=float)

print("3D Array")
print(arr)
