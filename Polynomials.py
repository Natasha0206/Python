import numpy as np

# Read the coefficients from input
coefficients = list(map(float, input().split()))
# Read the value of x from input
x = float(input())

# Evaluate the polynomial at the given point
result = np.polyval(coefficients, x)

# Print the result
print(result)