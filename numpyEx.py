import numpy as np

# 1.
arr = np.arange(100, 111)
print(arr)

# 2.
arr = np.random.randint(0, 10, size=(3, 3))
print(arr)

# 3.
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])
array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])
result = np.multiply(array1, array2)
print(result)

# 4.