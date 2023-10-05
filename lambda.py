"""
#Multiple parameter
x=lambda a,b,c,d:a+10+b+c+d
print(x(3,2,4,5))

x=lambda a,b:a*b+10
print(x(2,4))

x=lambda a,b:a-b+10
print(x(12,4))

message=lambda name:print("Hello",name)
message("Keerthy")

x=lambda a,b,c:a-b+10*c
print(x(12,4,2))
"""
"""
#passing string
name="welcome python"
big=lambda str:str.capitalize()
print(big(name))

x=lambda a:a*a*a
print(x(2))

#Lambda with higer order function

add=lambda *args:sum(args)
print(add(10,20,30,40,50))
"""
"""
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    square=lambda i:i**2
    list2.append(square(i))
print(list2)
"""
def adition(n):
    return n+n
numbers=[1,2,3,4,5]
list=[]
for i in numbers:
    list.append(adition(i))
print(list)