"""lambda functions: creating small anonymous functions
    """
"""short, simple operations
they dont have a name,  and are used when need a
simple function for a short period of time.
"""

# Regular function


def square(x):

    return x ** 2


# Lambda function
def square_lambda(x): return x ** 2


"""Syntax:
lambda [arguments]: [expression] 
"""

# other examples:


# Lambda function to add two numbers

def add(a, b): return a + b


print(add(3, 5))  # Output: 8


# Lambda function to print a name

def greeting(name): return f"Hello, {name}!"


print(greeting("Alice"))  # Output: Hello, Alice!
