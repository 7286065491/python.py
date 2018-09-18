ab=input()
g=[]
for y in range(0,len(ab)):
    if (ab[y]>='a' and ab[y]<='z') or (ab[y]>='A' and ab[y]<='Z'):
        c=0
    else:g.append(ab[y])
for y in range (0,len(g)):
    print(g[y],end='')
