def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
x=0
for i in range(2,2000001):
    if is_prime(i) is True:
        x += i
print(x)