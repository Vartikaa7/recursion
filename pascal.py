def fact(n):
	i=1
	fac=1
	while i<=n:
		fac*=i
		i+=1
	return fac
def pascal(n):
	for i in range(n):
		for j in range(i+1):
			print(fact(i)//(fact(j)*fact(i-j)),end=" ")
		print("\n")
n=int(input())
c=pascal(n)
