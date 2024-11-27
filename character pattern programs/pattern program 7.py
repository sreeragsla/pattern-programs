n=int(input())
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
    print()
    stars+=1
