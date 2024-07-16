def wordPattern(string,Pattern):
    word_dict = {}
    s_list = string.split()
    if len(set(Pattern)) != len(set(s_list)) or len(Pattern) != len(s_list):
        return False
    else:
        for idx, val in enumerate(s_list):
            if val not in word_dict:
                word_dict[val] = Pattern[idx]
            else:
                if word_dict[val] != Pattern[idx]:
                    return False
    return True


t1 = "abba"
s1 = "dog cat cat dog"
t2 = "abba"
s2 = "dog cat cat fish"
print(wordPattern(s1,t1))
print(wordPattern(s2,t2))