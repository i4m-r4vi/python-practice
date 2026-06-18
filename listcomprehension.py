"""
List Comprehension => It  is a concise / simple way of creating new list from a existing list

"""

x = [100,200,300,400,500]

# copy x into new list y and double the x elements
#y-> 

# y=[]

# for ele in x:
#     y.append(ele*2)
    
# print(y)

# converting into comprehension

z = [ele*2 for ele in x]
print(z)

# generate even numbers from 50 to 500 by LC
# expression iteration condition
evenum =[ele for ele in range(50,501) if ele%2==0]
print(evenum)
