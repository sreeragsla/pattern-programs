n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1



    
