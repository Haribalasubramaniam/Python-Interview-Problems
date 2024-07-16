def lengthOfLongestSubString(s):
    left=max_length=0
    output=set()
    for i in range(len(s)):
        while s[i] in output:
            output.remove(s[left])
            left+=1
        output.add(s[i])
        max_length=max(max_length,i-left+1)
    return max_length



s1 = "abcabcabc"
s2 = "pwwkew"
print(lengthOfLongestSubString(s1))
print(lengthOfLongestSubString(s2))