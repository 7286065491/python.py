a=int(input(""))
lst=[int(z) for z in input().split()]
s=0
for i in range(0,a):
     s+=lst[i]
print(int(s/a))
