n=int(input())
stars=n
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    stars-=1
