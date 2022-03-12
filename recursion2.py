
#2.natural numbers using recursion

def fun(n):
	if n==0:
		return 0
	return fun(n-1)+n
n=int(input("num"))
b=fun(n)
print(b)