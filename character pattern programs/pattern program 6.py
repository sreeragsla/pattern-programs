n=int(input())
dummy=1
for row in range(1,n+1):
    for st in range(1,n+1):
        if row%2!=0:
            print(chr(dummy+64),end=' ')
            dummy+=1
        else:
            print(chr(dummy+64),end=' ')
            dummy-=1
    print()

