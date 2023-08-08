'''
Desenvolver um programa que pergute ao ususário ao seu peso (em quilos) e sua altura (em metros). Ao final o programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímentros.
'''
import math

peso = float(input("Me informe o seu peso, em Kg?"))
h = float(input("Me informe sua altura, em metros?"))
pgramas = peso * 1000
hcentimetros = h * math.pow(10,3)
print("O senhor possui uma %dcm de altura e %sg de peso" % (pgramas, hcentimetros))
