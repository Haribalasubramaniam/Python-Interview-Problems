def isPalindrome(s):
    l = 0
    r = len(s)-1
    while l<r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l].lower() == s[r].lower():
            l+=1
            r-=1
        else:
            return False
    return True
    
s1 = "A man, a plan, a canal: Panama"
s2 = "Race a Car"
print(isPalindrome(s1))
print(isPalindrome(s2))
