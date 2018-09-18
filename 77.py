mn=int(input())
for x in range(1,mn+1):
    if(mn%x==0):
        if x<mn:
            g=' '
        else:
            g=''
        print(x,end=g)
