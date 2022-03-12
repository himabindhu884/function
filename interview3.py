# 3.multiple of the numbers what we can enterd that will be executed

n=int(input("enter number "))
b=n
i=1
l=''
while i<=b:
	l+=str(n)+"*"
	i+=1
print(l[0:len(l)-1],"=",n**n)
