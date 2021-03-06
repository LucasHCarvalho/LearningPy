'''
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente
'''


x = int(input("Digite um número:"))
y = int(input("Digite um número:"))
z = int(input("Digite um número:"))

if(x < y < z):
	print("crescente")
else:
	print("não está em ordem crescente")