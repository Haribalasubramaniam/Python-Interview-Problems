def diamond_pattern(n):
    for i in range(1,2*n):
        spaces = abs(n-i)
        stars = 2*(n-spaces)-1
        print(" "*spaces + "*"*stars)
        
n = int(input("Enter a Number : "))
diamond_pattern(n)