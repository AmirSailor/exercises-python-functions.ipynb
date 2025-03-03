a = []  # Initialize the list 'a'

# Function to generate triangle numbers
def triangle_numth(n):
    x = 0
    for i in range(1, n + 1):  # Include n by using range(1, n+1)
        x += i
        a.append(x)
    return a

# Function to count the divisors of a number
def div(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):  # Iterate up to the square root of n
        if n % i == 0:
            if n // i == i:  # If i and n//i are the same, count it only once
                count += 1
            else:
                count += 2  # Count both i and n//i as divisors
    return count

# Generate triangle numbers and check for divisors
triangle_numbers = triangle_numth(20000)  # Check for more triangle numbers

# Print divisors of triangle numbers as we go
for i in triangle_numbers:
    divisor_count = div(i)
    if divisor_count >= 500:
        print(f"Found! Triangle number: {i} has {divisor_count} divisors.")
        break  # Stop after finding the first triangle number with 500 divisors
