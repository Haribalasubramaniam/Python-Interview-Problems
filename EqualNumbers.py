def equal_nums(a,k):
    dict={}
    for i in range(len(a)):
        if a[i] in dict and abs(i-dict[a[i]])<=k:
            return True
        dict[a[i]] = i
    return False
a=[5,7,9,5]
k=3
print(equal_nums(a,k))
b=[2,4,2,8]
k=1
print(equal_nums(a,k))
c=[10,20,30,10,40,30]
k=2
print(equal_nums(a,k))