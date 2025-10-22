#task1 
def factorial(n):
    """
    Calculates the factorial of a non-negative integer using a loop.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# 1. Ask the user for input
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# 2. Call the function and print the output
fact_result = factorial(num)

if isinstance(fact_result, int):
    print(f"Factorial of {num} is: {fact_result}")
else:
    # This handles the case for negative numbers
    print(fact_result)

# Expected Output Example (as per assignment):
# Enter a number: 5
# Factorial of 5 is: 120