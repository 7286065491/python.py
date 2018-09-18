xy=int(input())
rev1=0
if xy<1000:
    while xy>0:
        rem=xy%10
        rev1=(rev1*10)+rem
        xy=xy//10
    print(rev1)
