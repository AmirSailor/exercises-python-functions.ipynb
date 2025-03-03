def odd(n):
    return (3 * n) + 1
def even(n):
    return n / 2
def collatz_sequence_length(n):
    count = 1  # Start count at 1 (including n itself)
    while n != 1:  # Continue until n reaches 1
        if n % 2 == 0:
            n = even(n)
        else:
            n = odd(n)
        count += 1  # Increase step count
    return count

def longest_collatz(limit):
    max_length = 0
    max_num = 0

    for i in range(limit, 1, -1):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            max_num = i
    print(f"The number {max_num} produces the longest Collatz sequence with {max_length} terms.")

longest_collatz(1000000)