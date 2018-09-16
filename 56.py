xy=input()
count=0
count1=0
for k in range(0,len(xy)):
    if((xy[k]>='a') and (xy[k]<='z') or (xy[k]>'A') and (xy[k]<'Z')):
            count=1
    elif((xy[k]=='1') or (xy[k]=='2') or (xy[k]=='3') or (xy[k]=='4') or (xy[k]=='5') or (xy[k]=='6') or (xy[k]=='7') or (xy[k]=='8') or (xy[k]=='9') or (xy[k]=='0')):
            count1=1
if count+count1==2:
     print("yes")
else:print("no")
