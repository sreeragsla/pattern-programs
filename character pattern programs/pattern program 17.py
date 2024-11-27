n=int(input())
stars=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        if row==st or row+st==6:
            print(chr(dummy+64),end=' ')
        else:
            print(' ',end=' ')
    print()
