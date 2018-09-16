mn=int(input())
k=0
while k<1000:
   if mn<2**k:
      print(2**k)
      break
   k+=1
