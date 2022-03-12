# 39. Your task is to make two functions, max and min (maximum and minimum in PHP and
# Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs,
# respectively, the largest and lowest number in that array/vector.❓❓❓❓

# #Examples:-
# maximum([4,6,2,1,9,63,-134,566]) returns 566

# minimum([-52, 56, 30, 29, -54, 0, -110]) returns -110

# maximum([5]) returns 5.

# minimum([42, 54, 65, 87, 0]) returns 0.

def fun():
    a=[4,6,2,1,9,63,-134,566]
    b=[-52, 56, 30, 29, -54, 0, -110]
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    j=0
    min=b[j]
    while j<len(b):
        if a[j]<min:
            min=b[j]
        j+=1
    print(max)
    print(min)
fun()