'''
Este codigo é para mostrar uma maneira alternativa
	de fazer o exercicio 2, sem usar tantos if's e
	possibilitando ao programador maior facilidade em
	produzir o codigo. Ao acrescentar uma variavel "maior",
	pode-se guardar sempre o maior valor, sem sabermos qual,
	de facto, é a variavel maior.

Este codigo funciona para um numero razoavel de variaveis (ver "for")
'''

x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))
w = int(input("W = "))

maior = x

if (y > maior):
	maior = y

if (z > maior):
	maior = z

if (w > maior):
	maior = w

print(maior)