# 3.palindrome number


def fun():   
    a=["abc","asd","121","mom","cac"]
    i=0
    c=0
    while i<len(a):
        if a[i]==a[i][::-1]:
            c+=1
        i+=1
    print(c)
fun()
