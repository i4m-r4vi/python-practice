"""
Lambda Function (Anonymous Function)
A lambda function is a small anonymous function used for simple expressions.
It is Anonymous Functions with single line expressions / code
It is used to pass a function as a parameter to the other function
syntax: var = lambda parameters1,parameters2,... parameters n:expression
"""

# def f1(a1,a2):
#     return a1+a2



# def f2():
#     print("hi")
#     print("hello")
#     print(f1(1,2))

# f2()
# add = lambda a,b:a+b
# print(add(10,20))

# print(add)

big = lambda num1,num2 : f'{num1} is Biggest' if num1>num2 else f'{num2} is Biggest'

print(big(4,1))

# Passing a fun as a parameter

f2 = lambda : print("I am Learning Lambda")
def f1(fun):
    print('h1')
    fun() #functioncall
    print('Bye')

    
f1(f2)

x = [19,20,12,133,134,35]
even = list(filter(lambda n: n%2==0,x))
print(even)

#update list elements by add 5 to each elements

du = list(map(lambda n:n+5,x))
print(du)