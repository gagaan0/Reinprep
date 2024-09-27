#Special string

def minascii(A:str, S:str)->int: 
    totaldistance=0

    for char_a in A: 
        mindistance=float('inf')

    for char_s in S:
        distance=abs(ord(char_a)-ord(char_s)) 
        mindistance=min(mindistance, distance)
    totaldistance+=mindistance
    return totaldistance

A="abcd" 
S="xyz" 
print(minascii(A,S))