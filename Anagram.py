def anagram(s,t):
    if len(s) != len(t):
        return False
    dict = {}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
            
    for j in t:
        if j in dict:
            dict[j] -= 1
            if dict[j]==0:
                dict.pop(j)
        else:
            return False
        
    return True

s1 = "anagram"
t1 = "nagaram"
s2 = "cat"
t2 = "rat"
print(anagram(s1,t1))
print(anagram(s2,t2))