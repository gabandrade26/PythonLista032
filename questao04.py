'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o program deverá exibir na tela o valor do índice de massa corporal desta pessoa (IMC). Fórmula: IMC = peso / altura² - Obs: peso em quilos e alturas em metros.
'''
import math

peso = float(input("Qual o seu peso, em Kg por favor?"))
h = float(input("Qual sua altura, em metros por favor?"))
imc = peso / math.pow(h,2)
print(f"O seu IMC é {imc:,.2f}")
