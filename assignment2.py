class employee:
    def method1():
        print("hello world")
    
    def method2():
        print("hello python")

employee1 = employee.method1()
employee2 = employee.method2()


class doctor:
    def method1(name):
        print(f'hello doctor {name}')
    
    def method2(doctorname,specialist):
        print(f'{doctorname} is a {specialist}')
        

doctor1 = doctor.method1("Natrayan")
doctor2 = doctor.method2("ramesh","ent doctor")
doctor3 = doctor.method2("suresh","dentist")
        