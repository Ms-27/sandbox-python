import random
import re


class Car:
    def __init__(self, color):
        self.color = color

    @classmethod
    def mycolor(cls, code):
        return cls(code)
    
    def display(self):
        return self.color
    
color_code = Car('Red')
color_code = Car.mycolor('Green')
#print(color_code.display())

#shuffle str
name = 'Olivier'
name = ''.join(sorted(name, key=lambda x: random.random())) 
#print(name)

'''
nb = '453'
if re.search(r'^\d{4}$', nb):
    print('Ok')
else:
    print('Problem')
'''

a = (lambda x, y: x if x > y else y)(8,6)
#print(a)


class A:
    pass
#print(A() == A())


S = "Rooose"
V = {i for i in S}
#print(len(V))

#arr = ['a', 'b', 'c', 'd', 'e']
#pop = " ".join(arr)
#result = len(list(re.findall(r'a', pop)))
#print(result)

arr = [';]', ':[', ';*', ':$', ';-D']
arr1 = [';D', ':-(', ':-)', ';~)']
result = len(list(re.findall('[:;][-~]?[)D]', " ".join(arr1))))
print(result)
