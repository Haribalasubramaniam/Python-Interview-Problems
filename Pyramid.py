n=int(input("Enter a Number : "))
for i in range(n):
    for j in range(n):
        if(i+j==n-1 or i+j==n+1 or i+j==n+3):
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(n-1):
        if(i>j and (i+j)%2!=0):
            print("*",end="")
        else:
            print(" ",end="")
    print()