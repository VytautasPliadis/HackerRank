import numpy as np

# Read input
x, y = map(int, input().split())
array_a = np.array([list(map(int, input().split())) for _ in range(x)])
array_b = np.array([list(map(int, input().split())) for _ in range(x)])

# Perform operations
addition_result = np.add(array_a, array_b)
subtraction_result = np.subtract(array_a, array_b)
multiplication_result = np.multiply(array_a, array_b)
integer_division_result = np.floor_divide(array_a, array_b)
modulus_result = np.mod(array_a, array_b)
power_result = np.power(array_a, array_b)

# Print output
print(addition_result)
print(subtraction_result)
print(multiplication_result)
print(integer_division_result)
print(modulus_result)
print(power_result)

'''
1 4
1 2 3 4
5 6 7 8
'''
