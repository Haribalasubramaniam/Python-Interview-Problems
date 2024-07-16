n=int(input("Enter a Number : "))
for i in range(n):
    for j in range(n):
        if(i==j or i==0 or j==n-1 or j>i):
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(n-1):
        if(i==n-1):
            continue
        elif(i==0 or j==0 or i+j<n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()