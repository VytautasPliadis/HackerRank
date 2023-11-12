# Global variable
global_variable = 10


def my_function():
    # Declare the variable as global before using it
    global global_variable

    # Accessing the global variable
    print(global_variable)

    # Reassigning the global variable
    global_variable = 20


my_function()

# The global variable has been modified by the function
print(global_variable)