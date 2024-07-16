def isHappy(n):
    def get_next(n):
        return sum(int(digit)**2 for digit in str(n))
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n==1

n = 19
print(isHappy(n))

"""
Explanation
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""