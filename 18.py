def recurring_cycle_length(d):
    """ Returns the length of the recurring cycle in 1/d. """
    if d % 2 == 0 or d % 5 == 0:
        return 0  # No cycle if d has factors of only 2 and 5
    
    length = 1
    remainder = 10 % d
    while remainder != 1:
        remainder = (remainder * 10) % d
        length += 1
    
    return length

def find_longest_recurring_cycle(limit):
    """ Finds the value of d < limit that has the longest recurring cycle in 1/d. """
    max_length = 0
    result_d = 0
    
    for d in range(2, limit):
        cycle_length = recurring_cycle_length(d)
        if cycle_length > max_length:
            max_length = cycle_length
            result_d = d
            
    return result_d

# Find the d < 1000 with the longest recurring cycle
print(find_longest_recurring_cycle(1000))
