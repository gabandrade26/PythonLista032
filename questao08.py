'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

preco = float(input("Qual o preço de custo do produto?"))
percentual = float(input("Quanto de acréscimo terá?"))
acrescimo = preco * percentual/100
venda = preco + acrescimo
texto_venda = f"R$ {venda:_.2f}"
texto_venda_br = texto_venda.replace(".",",").replace("_",".")
print(f"Esse será o preço de venda do produto: {texto_venda_br}")