n = int(input("Enter a 3-digit number: "))

if n >= 100 and n <= 999:
    original = n

    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    result = a**3 + b**3 + c**3

    if result == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
else:
    print("Please enter a 3-digit number")
