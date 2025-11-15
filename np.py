import numpy as np

""""
3x  + 2y  = 7
5x  + 3y = -1  
Ax  = B  => A^{-1 } * B                                                           
"""
A = np.array([[3, 2], [5, -3]])
B = np.array([7, -1], dtype  ="float")

print(A)
print(B)

A_inv = np.linalg.inv(A) #A^{-1}
print(A_inv)

print(A @ A_inv)

x = A_inv @ B
print('Решение нашей системы')
print(x)

"""
3x + 5y + 4z = 23 
-5x + 2y - 4z = 11
-2x -3y -5z =  -5
"""
A = np.array([[3, 5, 4], [-5, 2, -4], [-2, -3, -5]], dtype='float')
B = np.array([23, 11, -5], dtype='float')
A_inv = np.linalg.inv(A) #A^{-1}

x = A_inv @ B
print(x)

print(np.linalg.solve(A, B))

x = A_inv @ B
print('Решение нашей системы')
print(x)