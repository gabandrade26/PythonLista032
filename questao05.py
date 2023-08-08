'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo número
'''

num1 = int(input("Me informe um número:"))
num2 = int(input("Me informe um número:"))
soma = num1 + num2
sub1 = num1 - num2
sub2 = num2 - num1
mult = num1 * num2
div = num1 / num2
resto = num1 % num2
print(f"Essa é a soma do seus número: {soma:d}")
print(f"Essa é a subtração do primeiro pelo segundo número: {sub1:d}")
print(f"Essa é a subtração do segundo pelo primeiro número: {sub2:d}")
print(f"Essa é a multiplicação do seus número: {mult:d}")
print(f"Essa é a divisão do seus número: {div:.2f}")
print(f"Essa é a resto da divisão do seus número: {resto:d}")
