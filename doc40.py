#40.Write a function For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1❓❓❓❓

def fun():
    a=[9,1,1,9]
    i=0
    s=""
    while i<len(a):
        s=s+(str(a[i]**2))
        i+=1
    print(s)
fun()