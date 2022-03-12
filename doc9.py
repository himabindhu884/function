# 9.Write a Python program to generate and print a list of first and last 5 elements where 
# the values are square of numbers between 1 and 30 (both included)

# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900])


def fun():
    i=1
    b=[]
    while i<=30:
        square=i*i
        b.append(square)
        i+=1
    print(b,end=" ")
fun()