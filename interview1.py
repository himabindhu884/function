# we can add the integers and separate the names

def fun():
	a=["himabindhu",1,0.5,"spandana"]
	i=0
	sum=0
	while i<len(a):
		if type(a[i])==int or type(a[i])==float:
			sum=sum+a[i]
		else:
			print(a[i])
		i+=1
	print(sum)