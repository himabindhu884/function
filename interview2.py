#2.we can delete the first two elements of the list.

def fun():
	a=["spandana","himabindhu","gouthami","swathi"]
	i=0
	b=[ ]
	c=2
	while i<len(a):
		if i >= c:
			b.append(a[i])
		i+=1
	print(b)
fun()