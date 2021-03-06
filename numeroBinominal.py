def fatorial(n):
	total = 1
	while(n > 1):
		total *= n
		n -= 1
	return total

	
def numeroBinominal(n, k):
	nF = fatorial(n)
	kF = fatorial(k)
	nkF = fatorial(n-k)

	return nF/kF*nkF

n = int(input("Digite o valor de n")
k = int(input("Digite o valor de k")

numeroBinominal(n, k)
