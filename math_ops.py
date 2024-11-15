# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        return "Cannot Divide by 0"
    return a / b  # Potential division by zero error

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The result of division is: {result}")
