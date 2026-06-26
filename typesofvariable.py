"""
An instance variable is a variable that belongs to an object (instance) of a class. Each object gets its own copy of the instance variable, so changes made to one object's variable do not affect other objects.

Key Points
Defined inside methods (usually __init__) using self.
Belongs to a specific object.
Each object maintains its own copy.
Accessed using the object reference (e.g., s1.name).

Short defintion of a instance variable

An instance variable is a variable declared within a class and associated with an object instance, where each object has its own separate copy of the variable.
"""


# class school:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
        
#     def print11(self):
#         print("Accessing instance variable inside the class using the keyword")
#         print(self.a)
#         print(self.b)
        
        
        
# a = school(10,20)
# a.print11()
# print("Accessing instance variable outside the class using the keyword")
# print(a.a)
# print(a.b)


"""
Class Variable

A class variable is a variable that is declared inside a class but outside all methods. It belongs to the class itself and is shared by all objects (instances) of that class. Any change made to the class variable is reflected across all instances unless it is overridden at the instance level.

Example
class Student:
    school = "ABC School"  # Class variable

Here, school is a class variable because it is shared by every Student object.

"""

# class Student:
#     school = "ABC School"
    
#     def __init__(self):
#         self.x=10
        
# object_calling = Student()
# print("Class Variable Calling")
# print(Student.school)
# print("Object Variable Calling")
# print(object_calling.x)

        
# class PythonFSD:
#     trainername="Ashwanth"
#     class_time = "7Pm"
    
#     def __init__(self,name,mob):
#         self.name=name
#         self.mob=mob
#         print("Inside Init:",PythonFSD.trainername)
#         print("Using Self:",self.class_time)

#     def display(self):
#         print("Name:",self.name)
#         print("Mobile:",self.mob)
    
# p=PythonFSD("Ravi",9876543219)
# p.display()

# d=PythonFSD("Shankar",9876543211)
# d.display()
    


