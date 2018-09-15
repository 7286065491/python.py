x=int(input())
count=0
sum=0
while x>0:
    rem=x%10
    sum=sum+rem
    x=x//10
print(sum)
