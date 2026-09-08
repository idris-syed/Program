n = int(input("Enter a number: "))

n = abs(n)

if n == 0:
    print(0)
else:
    divisor = 1

    while n // divisor >= 10:
        divisor = divisor * 10

    while divisor > 0:
        digit = n // divisor
        print(digit)
        n = n % divisor
        divisor = divisor // 10
