#Missing aplhabets

s=input()
a="abcdefghijklmnopqrstuwxyz"
d=""
for i in a:
    if i not in a:
        d+=1
print(d)