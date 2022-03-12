#5.write a python function that takes a list and returns a new list with  unique elements of the first list❓❓❓

#output[1,2,3,4,5]

def fun(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]not in b:
            b.append(a[i])
        i+=1
    print(b)
fun([1,2,3,3,3,3,4,5])

