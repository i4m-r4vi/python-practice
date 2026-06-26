"""
### Types of Functions (Methods) in OOP

#### 1. Constructor Method (`__init__`)

A **constructor** is a special method that is automatically called when an object is created. It is used to initialize the instance variables of an object.

```python id="d2q6v8"
class Student:
    def __init__(self, name):
        self.name = name
```

---

#### 2. Instance Method

An **instance method** is a method that operates on a specific object and can access the object's instance variables using `self`.

```python id="bgv9ca"
class Student:
    def display(self):
        print(self.name)
```

---

#### 3. Class Method

A **class method** is a method that operates on the class itself rather than on individual objects and uses `cls` to access class-level data.

```python id="n5v5r9"
class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

---

#### 4. Static Method

A **static method** is a method that belongs to a class but does not depend on instance or class data and therefore does not use `self` or `cls`.

```python id="haxv2v"
class Student:
    @staticmethod
    def greet():
        print("Welcome")
```

---

### Summary

| Method Type                  | First Parameter | Purpose                                           |
| ---------------------------- | --------------- | ------------------------------------------------- |
| **Constructor (`__init__`)** | `self`          | Initializes object data when an object is created |
| **Instance Method**          | `self`          | Works with instance variables                     |
| **Class Method**             | `cls`           | Works with class variables                        |
| **Static Method**            | None            | Independent utility method                        |

**Types of Methods in OOP:**

1. Constructor Method (`__init__`)
2. Instance Method
3. Class Method
4. Static Method
"""

class TypeofMethod:
    num=10
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def display(self):
        print("X Value is:",self.x)
        print("Y Value is:",self.y)
        
    # class methods
    @classmethod
    def cm(cls):
        print
        print("class method",cls.num)   
        obj=cls(10,10)
        obj.display()
            

TypeofMethod.cm()
