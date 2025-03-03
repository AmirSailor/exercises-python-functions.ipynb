# Function to calculate the sum of the diagonals of an n x n spiral matrix
def diagonal_sum(n):
    total_sum = 1  # Start with the center value 1
    current_value = 1  # This represents the current center value of each layer
    for layer in range(3, n + 1, 2):  # Start from layer 3 to n (odd layers only)
        # The corners of the current layer
        for i in range(1, 5):
            current_value = (layer - 2) ** 2 + i * (layer - 1)
            total_sum += current_value
    return total_sum

# Calculate the sum for a 1001x1001 spiral
result = diagonal_sum(1001)
result
