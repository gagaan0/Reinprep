# Magic string

def magicstring(s): 
    freq={}
    for char in s:
        if char in freq: 
            freq[char]+=1
        else: 
            freq[char]=1 
        maxfreq=max(freq.values()) 
        minsteps=len(s)-maxfreq
        return minsteps
s=input()
result=magicstring(s)
print(result)