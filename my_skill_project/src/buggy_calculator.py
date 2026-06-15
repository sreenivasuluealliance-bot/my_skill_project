# buggy_calculator.py - Bugs ఉన్న Calculator

def add(a, b):
    return a + b          # Bug 1: fixed - now adds correctly

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b          # Bug 2: fixed - added zero check

def get_square(n):
    return n * n          # Bug 3: fixed - added missing colon

result = add(10, 5)
print("10 + 5 =", result)

result2 = divide(10, 2)   # Bug 4: fixed - changed divisor from 0 to 2
print("10 / 2 =", result2)

print("Square of " + str(4))   # Bug 5: fixed - converted int to string