x=int(input(""))
lst=[int(y) for y in input().split()]
s=0
for i in range(0,x):
      s+=lst[i]
print(int(s/x))
