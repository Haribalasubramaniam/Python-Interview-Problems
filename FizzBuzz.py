def fizzbuzz(n):
    ans = []
    for i in range(1,n+1):
        if i%15 == 0:
            ans.append("FizzBuzz")
        elif i%3 == 0:
            ans.append("Fizz")
        elif i%5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans
print(fizzbuzz(15))
print(fizzbuzz(7))
print(fizzbuzz(10))