'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dia
'''

idade_ano = int(input("Qual sua idade em anos?"))
idade_mes = int(input("Quantos meses falta para o seu aniversário?"))
idade_dia = int(input("Quantos dias faltam para o seu aniversário?"))
dias = (idade_ano * 365) + (idade_mes * 30) + idade_dia
print(f"Essa é sua idade em dias: {dias:d} dias")