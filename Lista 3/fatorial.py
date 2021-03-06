'''
Exercício 1
Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.
'''

tamanho = x = int(input("Digite o valor de n:"))

while(tamanho > 1):
	tamanho -= 1
	x *= tamanho

if(x == 0):
	x = 1

print(x)