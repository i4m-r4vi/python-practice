city= 'bengaluru'
# print(city[::-1])

# print(city[-9:-3])

# print(city[1:6])
# print(city[:1000])
# print(city[::len(city)])
# print(city[1:-3])
# print(city[0:len(city):2])
# print(city[4:0:-1])
# print(city[::-1])
# print(-len(city))

"""
List - > use to collection of elements we can store multiple / values
properties of list

1.contains homogeneous element -> same and heterogeneous -> different
2.List is a mutable
3.list allow duplicates elements
4.it is created by square braches or list()
"""

marks = [10,20,30,40,50]
marks1= list((10,20,20,40,"Hterogeneous"))
print(marks1)
print(marks)
print(type(marks))
print(marks[0])
print(marks[-1])
print(marks[2:5])


marks[0]=1

print(marks)

"""
tuple -> use to collection of elements we can store multiple / values
properties of list
1. it is immutable
2. created by ()
"""
pythonn1=(10,20,30,40,50)
print(pythonn1[1])

marks2=tuple(marks)
print(type(marks2))

app_config=(2001,4001,5001,'config')

"""
set => set is an un-ordered collection where elements are stored in random order fashion
        set doesn't allow duplicates
        set is created by {}
"""

sett={10,20,4,20}
print(sett)
print(type(sett))
print(len(sett))