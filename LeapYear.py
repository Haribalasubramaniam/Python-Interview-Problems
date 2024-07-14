def leap_year(n):
    if n%400 == 0:
        return True
    elif n%4 == 0 and n%100 != 0:
        return True
    else:
        return False
    
print(leap_year(20))
print(leap_year(400))
print(leap_year(200))