r,s=map(int,input().split())
if r>s:
    ks=r
else:ks=s
for x in range(1,ks+1):
    if(s%x==0) and (r%x==0):
        b=x
print(b)
