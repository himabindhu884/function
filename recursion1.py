# 1.to reverse the given string using recursion.

def fun(n):
	if len(n)==1:
		return n
	else:
		return fun(n[1:])+n[0]
n=(input("num"))
b=fun(n)
print(b)
