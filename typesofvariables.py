# Local Variable:
# A variable that is created inside a function or block.
# It can be accessed only within that function or block and exists only while the function is executing.

# Global Variable:
# A variable that is created outside all functions.
# It can be accessed throughout the program and remains available during the entire execution of the program.

# globals():
# An inbuilt function that returns a dictionary containing all global variables.
# It can be used to access global variables by their names.
# Example: globals()['x'] returns the value of the global variable x.

x = 10

def f1(x, y, z):
    a = 1000
    print("Global Variable:", globals()['x'])
    print("Local Variable:", x)
    print("Local Variable:", y)
    print("Local Variable:", z)
    print("Local Variable:", a)

f1(100, 200, 300)

# x here refers to the global variable because we are outside the function.
# The local variables x, y, z, and a inside f1() are destroyed after the function call ends.
print(x)