"""
def addition(n):
    return n+n
numbers=(1,2,3,4)
res=map(addition,numbers)
print(list(res))

numbers=(1,2,3,4,5)
result=map(lambda a:a+a,numbers)
print(list(result))
"""
"""
num1=[10,20,30]
num2=[40,50,60]
answer=map(lambda x,y:x+y,num1,num2)
print(list(answer))
"""
"""
def even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
numbers=[1,2,3,4,5]
sum=map(even,numbers)
print(list(sum))

lst=[1,2,3,4,5]
answer=map(lambda a:a%2==0,lst)
print(list(answer))
"""
"""
#Filter()
people_ages=[12,34,11,29,10,54]

def myfun(a):
    if a>=18:
        return True
    else:
        return False
adults=filter(myfun,people_ages)

print(list(adults))

def even(num):
    if num%2==0:
        return True
    else:
        return False
numbers=[1,2,3,4,5]
sum=filter(even,numbers)
print(list(sum))

"""
"""
#lambda function include 

numbers=[0,1,2,3,4,5,6,7,8,9,10]

result=filter(lambda x:x%2!=0,numbers)
print("odd numbers")
print(list(result))
result=filter(lambda x:x%2==0,numbers)
print("even numbers")
print(list(result))

"""
def fun(num):
    return num % 3==0
numbers2=[1,2,3,4,5,6,7,8,9]
answer=filter(lambda x:fun(x),numbers2)
print(list(answer))

#numbers=[0,1,2,3,4,5,6,7,8,9,10]

result=filter(lambda x:x%2!=0,range(1,22))
print("odd numbers")
print(list(result))
result=filter(lambda x:x%2==0,range(1,11))
print("even numbers")
print(list(result))
