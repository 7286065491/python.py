xy=int(input())
a,a1=input().split()
a,a1=int(a),int(a1)
if(xy>a and xy<a1) or (xy>a1 and xy<a):
    print("yes")
else:print("no")
