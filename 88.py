x,y=map(int,input().split())
if x>y:
    gy=x
else:gy=y
while gy>0:
    if(gy%x==0) and (gy%y==0):
        a=gy
        break
    gy+=1
print(a)
