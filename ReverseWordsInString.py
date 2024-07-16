""" 
def reverse_words_in_string(s):
    s = s.split()
    st = s[::-1]
    return ' '.join(st)
"""
def reverse_words_in_string(s):
    s = s.strip()
    words = [word for word in s.split(" ") if word]
    i,j = 0,len(words)-1
    while i<j:
        if words[i] != " " and words[j] != " ":
            words[i],words[j] = words[j],words[i]
            i += 1
            j -= 1
    return " ".join(words)

s1 = "the sky is blue !"
s2 = "i am hari"
print(reverse_words_in_string(s1))
print(reverse_words_in_string(s2))