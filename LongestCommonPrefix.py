def longest_common_prefix(strs):
    s = min(strs)
    output = ""
    index = 0
    for i in range(len(s)):
        for j in strs:
            if s[i] != j[i]:
                index = 1
                break
        if index == 1:
            break
        output += s[i]
    return output
    
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","cat"]
print(longest_common_prefix(strs1))
print(longest_common_prefix(strs2))