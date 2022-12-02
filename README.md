
# What is Decoratior with Example?

A Decorator is a just a function that takes another function as an argument, add some kind of functionality and the returns another function.
All of this without altering the source code of the original function that you passed in.

## Decorator Syntax

def outer_function(func):
    def inner_func():
        print("Inside inner function")
        return func()
    print("Before Return")
    return inner_func

def argumental_func():
    print("This is argument")

decorator_argument=outer_function(argumental_func)
decorator_argument()

## Alternative
@outer_function
def argumental_func():
    print("This is argument")

argumental_func()

OUTPUT:
Before Return
Inside inner function
This is argument


