'''
Fazer um algoritmo que pergunte o nome de um vendendor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, exibir ao final o seu nome, o sálario fixo, a comissão e o sálario completo (fixo + comissão sobre vendas) no final do mês
'''

nome = input("Qual o seu nome?")
salario = float(input("Qual o seu salário fixo?"))
vendas = float(input("Ganhou quanto em vendas efetuadas esse mês?"))
comissao = vendas * 15/100
salario_completo = salario + comissao
texto_salario = f"R$ {salario:_.2f}"
texto_salario_completo = f"R$ {salario_completo:_.2f}"
texto_comissao = f"R$ {comissao:_.2f}"
texto_salario_br = texto_salario.replace(".",",").replace("_",".")
texto_salario_completo_br = texto_salario_completo.replace(".",",").replace("_",".")
texto_comissao_br = texto_comissao.replace(".",",").replace("_",".")
print(f"Olá senhor {nome}, seu salário fixo é de {texto_salario_br}, a comissão que você ganhará será {texto_comissao_br} e o seu salário final é de { texto_salario_completo_br}")
