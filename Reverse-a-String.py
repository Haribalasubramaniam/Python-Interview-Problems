"""
Reverse a String using Slicing Method
def reverse_string(s):
    return s[::-1]

s=str(input("Enter a String : "))
print(reverse_string(s)) 

"""
def reverse_string(s):
    i = 0
    j = len(s)-1
    s = list(s)
    while i < j:
        s[i],s[j]=s[j],s[i]
        i += 1
        j -= 1
    return ''.join(s)

s = str(input("Enter a Number : "))
print(reverse_string(s))