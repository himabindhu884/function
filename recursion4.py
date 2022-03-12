#4.using recursion Fibonacci sequence.

def fun(n):
	if n<=1:
		return n
	else:
		return(fun(n-1)+fun(n-2))
b=5
if b<=0:
	print("positive integer")
else:
	print("fibonacci sequence")
	for i in range(b):
		print(fun(i))