n=int(input())
for row in range(1,n+1):
    dummy=row
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
