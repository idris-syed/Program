n = int(input("Enter a number: "))

while n != 1 and n != 4:
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total = total + digit * digit
        temp = temp // 10

    n = total

if n == 1:
    print("Happy number")
else:
    print("Not a happy number")
