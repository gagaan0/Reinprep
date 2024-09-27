#Minimun number of key presses

def minkeypress(s): 
    target=int(s) 
    press=0
    while target>0:
        if target % 100 == 0: 
            target //= 100 
        else:
            target//=10
        press+=1
    return press
s=input().strip()
print(minkeypress(s))