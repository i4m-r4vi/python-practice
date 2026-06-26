# object is physical entity or real world entity
# class is a blueprint or template used to create objects. It defines the attributes (data) and methods (functions) that the objects created from it will have.


class person:
    def __init__(self,name,age):
        self.name1 = name #name1 is a instance variable
        self.age1 = age #age1 is a instance variable
    
    def mydetails(self):
        print(f'My name is {self.name1},My age is {self.age1}')
    
name1=person("Ravi",19)

name1.mydetails()
print(name1.name1)
print(name1.age1)


# id(self)