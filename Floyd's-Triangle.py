def floyds_triangle(n):
    num = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(65+num),end="")
            num += 1
        print()

n = int(input("Enter a Number : "))
floyds_triangle(n)