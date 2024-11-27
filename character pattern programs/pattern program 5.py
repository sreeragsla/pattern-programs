n=int(input())
for row in range(1,n+1):
    dummy=row
    for st in range(1,n+1):
        if row%2==0:
            print(chr(dummy+64),end=' ')
            dummy+=2
        else:
            print(chr(dummy+64),end=' ')
            dummy+=1
    print()
