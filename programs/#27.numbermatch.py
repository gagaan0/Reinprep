#Number match

n=int(input())
l=list(map(int,input().split())) 
A,B=0,0
for i in set(l):
    if i%2==0:
        if l.count(i)%2==0: 
            A+=l 
        else: 
            B+=l
    else:
        if l.count(i)%2==0: 
            B+=l 
        else:
            A+=l
if A>B:
    print("A", A-B)
elif B>A:
    print("B",B-A)
else:
    print("T 0")