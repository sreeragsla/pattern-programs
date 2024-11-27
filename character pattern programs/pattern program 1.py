n=int(input())
dummy=1
for row in range(1,n+1):
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
    print()
    dummy+=1
