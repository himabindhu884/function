#2.print the sum of values using the sum()function

def fun(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+num[i]
        i+=1
    print(sum)
fun([1,2,3,4,5])

