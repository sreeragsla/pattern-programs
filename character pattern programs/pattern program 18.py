n=int(input())
stars=1
spaces=n//2
for row in range(1,n+1):
    dummy=1
    for st in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    if row<=n//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
    
