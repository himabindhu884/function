# Q28. Write a function called showNumbers that takes a parameter called limit. It should print
# all the numbers between 0 and limit with a label to identify the even and odd numbers. ❓❓❓❓

# For example, if the limit is 3, it should print: - 0 even,1 odd, 2 even, 3 odd .

def fun():
    i=0
    while i<5:
        if i%2==0:
            print(i,"even",",",end="")
        else:
            print(i,"odd",",",end="")
        i+=1
fun()