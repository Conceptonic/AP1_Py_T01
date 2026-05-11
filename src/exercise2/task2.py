n = int(input())
if n < 0:
    print(False)
else:
    original = n
    reversed_n = 0
    tmp = n
    while tmp > 0:
        reversed_n = reversed_n * 10 + tmp % 10
        tmp //= 10
    print(original == reversed_n)
