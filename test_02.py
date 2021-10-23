'''
def outer_func():
    def inner_func():
        return "You reached the inner function!"
    return inner_func


decorator_object = outer_func()
print(decorator_object)
# här anropas outer_function och skriver ut texten i inner_function
print(decorator_object())
'''
# -----------------------------------------------------------------------------
'''
def my_first_decorator(function):  # Outer
    def execute_action():  # Inner_function
        function()  # denna functin ska dekoreras..
        print("This is the end of the inner function!")
    return execute_action  # The decorated function


def multiply():
    print("This is the multiply function.")


def add():
    print("This is the add function.")


decorated_function = my_first_decorator(multiply)
decorated_function()
decorated_function = my_first_decorator(add)
decorated_function()
'''
# -----------------------------------------------------------------------------
'''
def my_first_decorator(function):   # Outer
    def execute_action():           # Inner
        function()
        print("This is the end of the inner function!")
    return execute_action

# detta är samma sak som ovan fast ett smidigare sätt
# med @.. så kan man bara använda med dekorator, inte utan


@my_first_decorator
def multiply():
    print("This is the multiply function.")


@my_first_decorator
def add():
    print("This is the add function.")


multiply()
'''
# -----------------------------------------------------------------------------
'''
# If the decorated function has arguments, the inner function
# should have the same arguments


def my_first_decorator(function):   # Outer
    # def execute_action(a, b):       # Inner
    def execute_action(*args):       # Inner
        # function(a, b)  # Forward the arguments
        function(*args)  # Forward the arguments
        print("This is the end of the inner function!")
    return execute_action


@my_first_decorator
def multiply(a, b):
    print(f"This is the multiply function: {a} * {b}.")


@my_first_decorator
def add(a, b):
    print(f"This is the add function: {a} + {b}.")


multiply(1, 2)
'''
# -----------------------------------------------------------------------------


def my_first_decorator(function):   # Outer
    def execute_action(*args):      # Inner
        result = function(*args)    # Save the return value
        print("This is the end of the inner function!")
        return result
    return execute_action


@my_first_decorator
def multiply(a, b):
    return a * b


@my_first_decorator
def add(a, b):
    return a + b


print(multiply(1, 2))
