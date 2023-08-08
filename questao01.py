'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o valor do acréscimo dos 10% da gorjeta do garçom
'''

valor = float(input("Qual o valor da conta a ser paga?"))
conta = valor + (valor * 10/100)
texto_conta = f"R$ {conta:_.2f}"
texto_conta_br = texto_conta.replace(".",",").replace("_",".")
print(f"Essa é a conta ser paga: {texto_conta_br}")

