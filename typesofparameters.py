# # 1. Positional Arguments
# # Arguments are passed to the function based on their position or order.

# def concate(s1,s2):
#     con = s1 + ' ' + s2
#     return con

# res = concate('Besant','Technology')
# print(res)


# # 2. Keyword Arguments
# # Arguments are passed by specifying the parameter names explicitly.

# def student(name,age,role):
#     print(f'My name is {name} my age is {age} role is {role}')

# s1 = student(age=1,name='Ravi',role='Student')


# # 3. Default Parameters
# # Parameters are assigned default values which are used when no argument is provided.

# def counselling(name,phoneno,degree,email,course='Python FSD'):
#     print(name,phoneno,degree,email,course)

# counselling('Ravi',8344563311,'BSC','ksravishankars@gmail.com','DataScience')


# # 4. Arbitrary Positional Arguments (*args)
# # Allows a function to accept any number of positional arguments.

# def functionsss(*email):
#     if(len(email)<2):
#         for emails in email:
#             print("The email is sended to",emails.lower())
#     else:
#         print("email should be less than 2")

# functionsss("Ravi@gamil.com","example@gmail.com","powepoint@gmail.com")


# # 5. Arbitrary Keyword Arguments (**kwargs)
# # Allows a function to accept any number of keyword arguments.

# def f2(**args):
#     for i in args:
#         print(i,":",args[i])

# f2(name="Ravi",age=20)


# # 6. Lambda Function (Anonymous Function)
# # A lambda function is a small anonymous function used for simple expressions.

# add = lambda a,b:a+b

# print(add(10,10))


# def patient_info(name,age,email='demo@gmail.com',*symptoms,**address):
#     for symtom in symptoms:
#         for hno,cross in address.items():
#             print(f'Patient name is {name},age is {age},email is {email},symptoms are {symtom},address are {hno,cross}')
    
# patient_info("Ravi",18,'ayswarym04@gmail.com','cought','fever',hno=205,cross='2nd cross')

def patient_info(name, age, email='demo@gmail.com', *symptoms, **address):
    print(f"Patient name is {name}")
    print(f"Age is {age}")
    print(f"Email is {email}")
    print(f"Symptoms are {', '.join(symptoms)}")

    for key, value in address.items():
        print(f"{key}: {value}")

patient_info(
    "Ravi",
    18,
    'ayswarym04@gmail.com',
    'cough',
    'fever',
    hno=205,
    cross='2nd cross'
)