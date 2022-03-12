#5.how to call one function to another function

def sum(a,b):
    c=a+b
    return c
def multie():
    e=sum(3,4)
    return e
print(multie())