def armstrong_number(n):
    s = len(str(n))
    temp = n
    sum = 0
    while temp>0:
        digit = temp%10
        sum += digit**s
        temp //= 10
        
    return sum==n
print(armstrong_number(407))
print(armstrong_number(663))