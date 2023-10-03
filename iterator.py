"""
list=["Welcome","To","Python","World"]
ite=iter(list)
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
"""
"""
#Another method
list=["Welcome","To","Python","World"]
ite=iter(list)
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
"""
class num:
    def __init__(self) :
        self.num=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=20:
            value=self.num
            self.num +=2
            return value
        else:
            raise StopIteration
obj=num()

for i in obj:
    print(i)