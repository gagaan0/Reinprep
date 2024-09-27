#Maths test

def primenum(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def smallprime(N):
    num=N+1
    while not primenum(num):
        num+=1
    return num 
N=int(input()) 
result=smallprime(N) 
print(result)