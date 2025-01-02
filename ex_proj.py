"""THIS PROJECT IS FOR TESTING THE UNITEST """
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b==0: raise ValueError("THIS PROJECT IS FOR TESTING THE UNIT")
    return a / b

def square_of_numbers(a):
    if not isinstance(a, (int,float)):
        raise ValueError("Enter a number")
    return a ** 2

