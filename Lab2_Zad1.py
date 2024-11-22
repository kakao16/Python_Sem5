# Stanisław Kusiak

import os

class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __str__(self):
        return f"{self.real} + i * {self.imag}"
    
    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.imag - other.imag)
    

num1 = ComplexNum(12, 14)
num2 = ComplexNum(2, -2)

num3 = num1 + num2
num4 = num1 - num2

print(num3)
print(num4)
    
