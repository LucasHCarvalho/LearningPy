tamanho = x = int(input("Digite o valor de n:"))

while(tamanho > 1):
	tamanho -= 1
	x *= tamanho

if(x == 0):
	x = 1

print(x)