def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  # Avoid redundant calculations
            product = i * j
            if product <= max_palindrome:
                break  # Since numbers are decreasing, no need to check further
            if is_palindrome(product):
                max_palindrome = product
    return max_palindrome

print(largest_palindrome_product())