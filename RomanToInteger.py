def roman_to_integer(s):
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    answer = 0
    for i in range(len(s)):
        if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
            answer -= roman[s[i]]
        else:
            answer += roman[s[i]]
    return answer

s1 = "IX"
print(roman_to_integer(s1))
s2 = "MCMXCIV"
print(roman_to_integer(s2))