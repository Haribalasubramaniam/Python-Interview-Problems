def prime_number(n):
    flag = False
    if n == 1:
        print(n, "is not a Prime Number")
    for i in range(2,n):
        if n%i == 0:
            flag=True
            break
    if flag:
        print(n,"is not a Prime Number")
    else:
        print(n,"is a Prime Number")    
    
    
    
n = int(input("Enter a number : "))
prime_number(n)