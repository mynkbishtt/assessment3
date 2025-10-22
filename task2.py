import math

# 1. Ask the user for a number as input
try:
    user_input = float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# 2. Use the math module to calculate the required values
try:
    # Calculate Square root of the number [cite: 17]
    sqrt_result = math.sqrt(user_input)
    
    # Calculate Natural logarithm (log base e) of the number [cite: 18]
    log_result = math.log(user_input)
    
    # Calculate Sine of the number (in radians) [cite: 19]
    sine_result = math.sin(user_input)

    # 3. Display the calculated results [cite: 20]
    print(f"Square root: {sqrt_result}")
    print(f"Logarithm: {log_result}")
    print(f"Sine: {sine_result}")

except ValueError as e:
    # Handles errors like calculating the square root or logarithm of a negative number
    print(f"Error in calculation: {e}. Please ensure the number is non-negative for log and square root.")

# Expected Output Example (if 25 is entered):
# Enter a number: 25
# Square root: 5.0
# Logarithm: 3.2188758248682006
# Sine: -0.13235175009777303