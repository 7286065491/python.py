xy=list(input())
g=len(xy)
ss=len(xy)/2
s=int(len(xy)/2)
if g%2==0:
    xy[s-1]="*"
    xy[s]="*"
else:xy[s]="*"
for i in range(0,len(xy)):
    print(xy[i],end='')
