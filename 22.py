prime_list = []

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        else:
            prime_list.append(n)
#def permutations(m):
    
is_prime(7)
print(prime_list)