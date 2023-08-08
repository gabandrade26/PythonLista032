'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
'''

valor = float(input("Qual o valor da sua compra?"))
prestacao = int(input("Quantas prestações você escolheu?"))
valor_prestacao = valor / prestacao
texto_valor_prestacao = f"R$ {valor_prestacao:_.2f}"
texto_valor_prestacao_br = texto_valor_prestacao.replace(".",",").replace("_",".")
print(f"O valor das prestações serão {texto_valor_prestacao_br}")