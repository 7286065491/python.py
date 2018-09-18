xy=input()
evn=""
odd=""
for v in range(0,len(xy)):
    if (v)%2==0:
        evn=evn+(xy[v])
    else:
        odd=odd+(xy[v])
print(evn,odd)
