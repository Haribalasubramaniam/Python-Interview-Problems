def hammingWeight(n):
    res = 0
    for i in range(32):
        if(n >> i)&1:
            res+=1
    return res

print(hammingWeight(11))
print(hammingWeight(128))