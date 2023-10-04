"""
def num():
    yield 1
    yield 2
    yield 3
    yield 4
obj=num()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
"""
"""
def number():
    yield "welcome"
    yield 5.0
    yield "Python"
for i in number():
    print(i)
"""
"""
def odd_even():
    for i  in range(51):
        if(i%5==0):
            yield i

for i in odd_even():
    print(i)
"""
"""
def demo():
    n=1
    while n<=9:
        value=n*n
        yield value
        n+=1
obj=demo()
for i in obj:
    print(i)
"""
"""
def fibo(maxi):
    a,b=0,1
    while True:
        c=a+b
        if c<maxi:
            print("Before")
            yield c
            print("A")
            a=b
            b=c
        else:
            break
    obj=fibo(10)
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
"""
message=lambda name:print("Hello",name)
message("Keerthy")