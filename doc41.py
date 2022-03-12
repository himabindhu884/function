# 41)Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

def fun(): 
    a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
    i=0
    c=0
    max=[ ]
    while i<len(a):
        if a[i]>max:
            max=a[i]
            c+=1
        i+=1
    j=0
    c1=0
    min=a[j]
    while j<len(a):
        if a[j]>max:
            min=a[j]
            c1+=1
        j+=1
    print((len(max),max))
    print((len(min),min))
fun()