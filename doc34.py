# 34.Write a function which converts the input string to uppercase.

# For example:-
# [10, 14, 2, 23, 19] --> 42 (= 23 + 19)
# [99, 2, 2, 23, 19] --> 122 (= 99 + 23)

# Input sequence contains minimum two elements and every element is an integer.❓❓❓❓

def fun():
    a=[10,14,2,23,19]
    b=[99,2,2,23,19]
    i=0
    max=0
    sum=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        else:
            sum=a[i]
        i+=1
    j=0
    max1=0
    sum1=0
    while j<len(a):
        if a[j]<max:
            if a[j]>max1:
                max1=b[j]
        else:
            sum1=b[j]
        j+=1
    print('total',max+sum)
    print('total',max1+sum1)
fun()