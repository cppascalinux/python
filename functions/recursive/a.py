def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
a=fact(int(input()))
print('result is %d'%a)