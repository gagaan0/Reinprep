#Toss and score

s=input()
src=0
for i in range(len(s)):
    if s[i]=="H":
        src+=2
        if s[i-2:i+1]=="HHH":
            break
    elif s[i]=="T":
        src-=1
print(src)