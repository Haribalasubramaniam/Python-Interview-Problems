def snakePattern(arr):
    col=len(arr[0])
    row=len(arr)
    for i in range(row):
        if i%2==0:
            for j in range(col):
                print(arr[i][j],end=" ")
            print()
        else:
            for j in range(col-1,-1,-1):
                print(arr[i][j],end=" ")
            print()
    

arr1=[[1,2,3],[4,5,6],[7,8,9]]
snakePattern(arr1)