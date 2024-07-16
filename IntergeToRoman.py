def int_to_roman(n):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []
    for i in range(len(values)):
        while n >= values[i]:
            n -= values[i]
            result.append(symbols[i])
    return ''.join(result)
    
    
n1 = 3749
n2 = 58
print(int_to_roman(n1))
print(int_to_roman(n2))