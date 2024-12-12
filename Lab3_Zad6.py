# Stanisław Kusiak

def upper_decorator(func):
    def wrapper(*args, **kwargs):
        temp = func(*args, **kwargs)
        return temp.upper()
    
    return wrapper
    
class Person:
    def __init__(self, name):
        self.name = name
    
    
    def hello(self):
        return f"Hello! My name is {self.name}"
    
    @upper_decorator
    def HELLO(self):
        return self.hello()
    
Jeff = Person("Jeff")

print(Jeff.hello())
print(Jeff.HELLO())