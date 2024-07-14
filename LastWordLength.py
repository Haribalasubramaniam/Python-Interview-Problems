def last_word_length(s):
    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] != " ":
            count+=1
            if s[i-1] == " ":
                break
    return count
    
s1 = " Hii Good Morning"
s2 = " How are You "
print(last_word_length(s1))
print(last_word_length(s2))