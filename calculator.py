from calculations.summation import summation
from calculations.subtraction import subtraction
from calculations.multiplication import multiplication
from calculations.division import division
from calculations.exponential import exponential
from calculations.root import root

num1 = float(input('número 1: '))
num2 = float(input('número 2: '))

operation_1 = summation(num1, num2)
operation_2 = subtraction(num1, num2)
operation_3 = multiplication(num1, num2)
operation_4 = division(num1, num2)
operation_5 = exponential(num1, num2)
operation_6 = root(num1, num2)

print("A soma dos números é:", operation_1)
print("A diferença dos números é:", operation_2)
print("O produto dos números é:", operation_3)
print("O quociente dos números é:", operation_4)
print("A potência dos números é:", operation_5)
print("A raiz dos números é:", operation_6)
