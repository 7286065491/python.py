xy=input()
ch=[]
for m in range(0,len(xy)):
    ch.append(xy[m])
a=[]
m=len(xy)-1
count=0
while m>=0:
    a.append(xy[m])
    m-=1
for m in range(0,len(ch)):
    if ch[m]==a[m]:
        count+=1
if count==len(ch):
    print("yes")
else:print("no")
