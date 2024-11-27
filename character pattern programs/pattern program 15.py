n=int(input())
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,n+1):
        if row==st:
            print(chr(dummy+64),end=' ')
        else:
            print(' ',end=' ')
    print()


        
