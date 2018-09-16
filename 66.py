x=int(input(""))
count=0
for k in range(1,x+1):
    if(x%k==0):
       count+=1
if (count==2):
    print("yes")
else:
    print("no")
