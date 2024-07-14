def valid_parentheses(s):
    dict = {")":"(","}":"{","]":"["}
    stack = []
    for i in s:
        if i in dict:
            if stack and stack[-1] == dict[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
        
    return True if not stack else False

s = "([{}])"
print(valid_parentheses(s))
t= "(([{[]}]))"
print(valid_parentheses(t))
