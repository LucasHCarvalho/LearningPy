'''
Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

x = int(input("Digite um número:"))

if(x % 5 == 0):
	print("FizzBuzz")
else:
	print(x)