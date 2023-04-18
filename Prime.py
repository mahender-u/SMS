x=int(input( "enter the source value"))
y=int(input ("enter the destionation"))

r=1

while(x<y):
    i=2
    count = 0
    while(i<=x/2):
       if (x % i == 0):
           count = count + 1
           break
       i = i + 1

    if count == 0:
        print(x,end=" ")
    x=x+1


