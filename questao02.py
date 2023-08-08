'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como reposta às horas atuais o valor 09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta quantos minutos já se passaram desde às 00:00h deste dia.
'''

hora = int(input("Quantas horas são agora, sem ter os minutos?"))
minuto = int(input("Quantos minutos se passaram?"))
dia = (hora * 60) + minuto
print(f"Os minutos que se passaram desde 00:00h são {dia:d} minutos")



