def sumofdividors(n):
    abundant_numbers = []
    for i in range (12, n + 1):
        total = 1
        for j in range(2,int((i**0.5)+1)):
            if i % j == 0:
                total += j
                if j != i//j:
                    total += i// j
        if total > i:  
            abundant_numbers.append(i)
    return abundant_numbers

res = sumofdividors(28123)

def checker(n):
    abundant_sum = set()
    for i in n:
        for j in n:
            sum_abundant = i + j
            if sum_abundant > 28123:
                break
            abundant_sum.add(sum_abundant)
    return abundant_sum

abundant_sums = checker(res)

#s = sum(i for i in range(1, 28124) if i not in abundant_sums)  # Use set for O(1) lookup
#print(s)

result = checker(res) 
s = 0
for i in range(0, 28123):
    if i not in result:  # Linear time lookup (O(n))
        s += i

print(s)
    