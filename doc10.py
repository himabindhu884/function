# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

# "4",  "5" --> "9"
# "34", "5" --> "39"
# Notes:

# If either input is an empty string, consider it as zero.

def fun(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+(a[i])
        i+=1
    print(sum)
fun([4,5])
fun([34,5])