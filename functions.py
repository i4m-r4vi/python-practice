# 1
def sum(x,y,z):
    c=x+y+z
    print(c)
    
sum(2,3,4)

# 2
def student(a,c,b):
    print(f'My name is {a},I am studing {b},Location is {c}')

student('Ravi','Bangalore',b='Cloud Computing')

# 3
def school(name,age,place):
    print(f'My name is {name},Age is {age},Location is {place}')
    
school('Lokesh Kanagaraj','35',place='Chocolate Factory')

# 4
def person(name,age,place='Bangalore'):
    print(f'Name is {name},Age is {age},Place is {place}')

person('Ravi',23)

# 5
def student(name, cls='10th', *marks):
    print("Name:", name)
    print("Class:", cls)
    print("Marks:", marks)
student("Ravi", "12th", 12, 13, 34)

# 6
def students(batch_name, student_name, *hobbies, **marks):
    print("Batch Name :", batch_name)
    print("Student Name :", student_name)
    print("Hobbies :", hobbies)
    print("Marks :")
    for subject, mark in marks.items():
        print(subject, ":", mark)

students(
    "aliens",
    "suresh",
    "tennis",
    "cricket",
    java=24,
    python=25,
    computers=23
)

students(
    "tom and jerry",
    "vignesh",
    "volley ball",
    "basket ball",
    java=25,
    python=24,
    computers=20
)

# 7
def college(proff_name, profesor_dept=None, **knowledge):
    print("Professor Name :", proff_name)
    print("Department :", profesor_dept)
    print("Subject Knowledge :")
    for subject, percentage in knowledge.items():
        print(subject, ":", percentage)


college(
    "govind",
    profesor_dept="computer science",
    data_structures="70%",
    mathematics="30%"
)

college(
    "hari",
    data_structures="30%",
    mathematics="80%"
) 