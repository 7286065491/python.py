r,s=input().split()
r,s=int(r),int(s)
pro=r*s
count=0
for m in range(0,pro):
    if m*m==pro:
        count=1
if count==1:
    print("yes")
else:print("no")
