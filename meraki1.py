#Q1 . You have to print the largest value out of the given list using the max function.
def fun(a):
	i=0
	max=0
	while i<len(a):
		if a[i]>max:
			max=a[i]
		i+=1
	print(max)
fun([3,5,7,34,2,89,2,5])

