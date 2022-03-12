#2.write of a python program to find the max of three numbers

def fun(a):
	i=0
	max=0
	while i<len(a):
		if a[i]>max:
			max=a[i]
		i+=1
	print(max)
fun([5,7,10])