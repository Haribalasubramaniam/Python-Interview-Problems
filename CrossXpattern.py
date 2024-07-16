s=str(input())
for i in range(len(s)):
    j=len(s)-i-1
    for k in range(len(s)):
        if(i==k or j==k):
            print(s[i],end=" ")
        else:
            print(" ",end=" ")
    print()    
    


    