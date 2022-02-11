class Cookie:
    # what is the difference between function and method?
    # # the 'self' keyword makes this a method
    # # methods are part of classes, but functions not necessarily so
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print(cookie_one.color)
print(cookie_two.color)

print("Cookie one is", cookie_one.get_color())
print("Cookie two is", cookie_two.get_color())

cookie_one.set_color('yellow')
print("Cookie one is now", cookie_one.get_color())
print("Cookie two is", cookie_two.get_color())


# this is an exmaple of object that isn't a pointer
num1 = 11
num2 = num1

print("Before value is updated:")
print("num1 =", num1)
print("num2 =", num2)

num1 = 22
print("After value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# Example of pointer!!
dict1 = {'value':11}
dict2 = dict1
print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

dict1['value'] = 22
print("After value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)
