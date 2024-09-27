#Target sum

l=list(map(int,input().split()))
s=int(input())
ans=[]
for i in range(len(1)): 
    for j in range(i+1,len(1)): 
        if l[i]+l[j] == s: 
            ans.append(i) 
            ans.append(j)
print(ans)