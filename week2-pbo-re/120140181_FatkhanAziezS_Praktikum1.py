import math

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def log(self, base=math.e):
        return Calculator(math.log(self.value, base))

    def __str__(self):
        return f"Hasil: {self.value}"


# Contoh penggunaan
a = Calculator(10)
b = Calculator(2)

print(a + b)       # 12
print(a - b)       # 8
print(a * b)       # 20
print(a / b)       # 5
print(a ** b)      # 100
print(a.log())     # ln(10)
