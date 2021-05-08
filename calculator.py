from calculations.summation import summation
from calculations.subtraction import subtraction
from calculations.multiplication import multiplication

num1 = float(input('numero 1: '))
num2 = float(input('numero 2: '))

operation_1 = summation(num1, num2)
operation_2 = subtraction(num1, num2)
operation_3 = multiplication(num1, num2)

print("A soma dos números é:", operation_1)
print("A subtração dos números é:", operation_2)
print("O produto dos números é:", operation_3)
