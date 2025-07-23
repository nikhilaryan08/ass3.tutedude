import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Use math module to calculate required values
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# 3. Display the results
print("Square root:", sqrt_val)
print("Natural logarithm:", log_val)
print("Sine (in radians):", sine_val)
