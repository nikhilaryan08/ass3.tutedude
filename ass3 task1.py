# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample call
number = 5
print("Factorial of", number, "is:", factorial(number))
