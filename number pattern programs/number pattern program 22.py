n=int(input())
stars=1
spaces=(n*2)-2
for row in range(1,n+1):
    dummy=1
    dum=row
    for col in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dum,end=' ')
        dum-=1
    print()
    stars+=1
    spaces-=2

        
