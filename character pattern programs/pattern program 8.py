n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
    print()
    stars+=1
    spaces-=1
