
def fibo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]

a = 1    
while len(str(fibo(a))) < 1000:
    a += 1

print(a)
