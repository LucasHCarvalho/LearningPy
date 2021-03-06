'''
Exercício 2
Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
'''

x = int(input("Digite o valor de n:"))
ultimo = 1

while(x >= 1):
	print(ultimo)
	ultimo += 2
	x -= 1
