def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
print(gcd(10, 5))

def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(10, 4))