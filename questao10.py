'''
 Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

num_eleitores = int(input("Quantos números de eleitores têm?"))
votos_brancos = int(input("Quantos votos brancos foram?"))
votos_nulos = int(input("Quantos forma votos nulos?"))
votos_validos = int(input("Quantos votos foram válidos?"))
percentual = (num_eleitores + votos_validos + votos_nulos + votos_brancos) / 100
print(f"Esse foi o percentual de todos eleitores: {percentual:_.2f}")
