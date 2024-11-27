n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
