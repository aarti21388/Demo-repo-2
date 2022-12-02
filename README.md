# Decorator Syntax

def outer_function(func):
    def inner_func():
        print("Inside inner function")
        return func()
    print("Before Return")
    return inner_func

@outer_function
def argumental_func():
    print("This is argument")

argumental_func()

OUTPUT:
Before Return
Inside inner function
This is argument

