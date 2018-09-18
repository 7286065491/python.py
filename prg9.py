M,H=input().split()
M,H=int(M),int(H)
sum=0
list=[int(y) for y in input().split()]
for x in range(0,H):
    sum=sum+list[x]
print(sum)
