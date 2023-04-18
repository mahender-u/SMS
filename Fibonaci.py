# fibonacci series
a=0
b=1
c=1
n=int(input('enter the value'))
print(a,b,end=" ")
while(c<=n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
