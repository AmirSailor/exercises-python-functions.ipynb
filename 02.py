def gcd(a, b):
    """Computes the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Computes the least common multiple (LCM) of two numbers."""
    return a * b // gcd(a, b)

def smallest_multiple(n):
    """
    Finds the smallest positive number that is evenly divisible by all numbers from 1 to n.
    
    Parameters:
    n (int): The upper limit of the range.
    
    Returns:
    int: The smallest multiple that is divisible by all numbers from 1 to n.
    """
    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)
    
    return multiple

# Find and print the smallest number evenly divisible by all numbers from 1 to 20
print(smallest_multiple(20))
