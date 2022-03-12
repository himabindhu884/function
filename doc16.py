#16.Print multiplication table of 12 using function.   
     
def fun():
    a=int(input('num'))
    i=1
    while i<=10:
        print(a,"*",i,"=",a*i)
        i+=1
fun()
