a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x

lcm = abs(a * b) // gcd

print("LCM =", lcm)
