x = input("Digite um número inteiro:")

tamanho = int(len(x)) - 1
x = int(x)

total = 0
divisor = 10

while(divisor >= 10):
	divisor = 10 ** tamanho
	tamanho -= 1
	valor = x // divisor
	total += valor
	x -= divisor * valor 

total += x % 10

print(total)