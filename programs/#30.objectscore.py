#Object score

N,M=map(int, input().split())
a=list(map(int,input().split()))
p=[]
for j in range(M):
    price,weight=list(map(int,input().split()))
    p.append([price,weight])
res=[]
for i in a:
    t=0
    for prc,wt in p:
        if prc<=i:
            t+=wt
    res.append(t)
print(*res,sep=" ")