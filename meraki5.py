#5.use the main function and find the minimum value of the list

def fun(a):
	i=0
	c=0
	b=a[i]
	while i<len(a):
		if a[i]<b:
			b=a[i]
			c+=1
		i+=1
	print(b)
fun([8, 6, 4, 8, 4, 50, 2, 7])