'''
for iterating in sequence
list tupple set range list
break continue


1. Using in operator -> it is straight forward apporach

cons this approach will not allow us to itterate element in tupple
elements in reverse order
getting alternative elements
it wont provides positions / index of elements 
2. using range() 
'''


# nums = [100,200,300,400,500,600]

# for ele in nums:
#     print(ele)

# print("break")
# for i in nums:
#     if i%200 == 0:
#         break
#     else:
#         print(i)
  
# print("continue")      
# for i in nums:
#     if i%200 == 0:
#         continue
#     else:
#         print(i)
        
        
# t1 = tuple((10,20,30,40,50))

# for i in t1:
#     print(i)

# name = 'RAVISHANKAR'
# for i in name:
#     print(i)


# s = {10,20,30,40,50,60}

# for ele in s:
#     print(ele)

nums = [6000,10,500,100,450,350,1050,400,500,600,5000]

sum = 0

# for num in nums:
#     sum=sum+num
# print(sum)

# find out the biggges element

# for num in nums:
#     if(sum<num):
#         sum=num
# print(sum)


# # find out the smallest 
# sum=nums[0]
# max=nums[0]
# for num in nums:
#     if(sum>num):
#         sum=num
#     if(max<num):
#         max = num
# print("smallest value:",sum)
# print("largest value:",max)


# read the value from keyboard and find that value is present in list
# if present display element found otherwise display element not found

# n = int(input("enter the number:"))

# for i in nums:
#     if n==i:
#         print("elements found")
#         break
# else:
#     print("elements not found")
    
    
# for i in range(len(nums)):
#     print(i,":",nums[i])    
#     pass
# print("Ended")
        
# display alternative elements

# for i in range(0,len(nums),2):
#     print(i,":",nums[i])    
#     pass
# print("Ended")

# display elements in reverse
# for i in range(len(nums)-1,0,-1):
#     print(nums[i])

# dictory with for loop
students = {
    'name':'ravishankar',
    'age':21,
    'degree':'BSC'
}

# for i in students:
#     print(i,'=',students[i])

# for k , v in students.items():
#     print(k,v)

# read a key from keyboard amd search it is present in the dict or not

k = input("Enter a key for search:").lower()

for i,v in students.items():
    if(k == i):
        print("It is present in Keys")
        break
    elif(k == v):
        print("It is present in values")
        break
else:
    print("It is not present in anything")