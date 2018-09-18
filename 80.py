rs=[int(y) for y in input()]
lst=[]
for x in range(0,len(rs)):
    if rs[x]%2!=0:
        lst.append(rs[x])
for x in range(0,len(lst)):
    if x<len(lst)-1:
        h=" "
    else:h=''
    print(lst[x],end=h)
