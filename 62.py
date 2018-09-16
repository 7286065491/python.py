x=input()
count=0
for k in range(0,len(x)):
      if(x[k]=='0' or x[k]=='1'):
              count+=1
      if count==len(x):
           print("yes")
      else:print("no")
