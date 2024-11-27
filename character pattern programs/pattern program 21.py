n=int(input())
stars=(n*2)-1
spaces=0
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
    spaces+=1
    stars-=2
