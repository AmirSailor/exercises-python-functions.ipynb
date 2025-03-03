def Pythagorean(n):
    for a in range(1, n//2):
        print(a)  # Iterate a from 1 to n//2
        for b in range(a, n//2):
            print(b)  # Iterate b from a to n//2
            c = n - a - b  # Calculate c such that a + b + c = n
            if a**2 + b**2 == c**2:  # Check if it satisfies the Pythagorean theorem
                print(f"The Pythagorean triplet is: a = {a}, b = {b}, c = {c}")
                print(f"The product a * b * c is: {a * b * c}")
                return  # Exit once the triplet is found

Pythagorean(1000)
