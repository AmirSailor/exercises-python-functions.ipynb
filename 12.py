from functools import lru_cache

@lru_cache(None)  # Memoization to speed up recursive calls
def count_paths(x, y):
    if x == 0 or y == 0:  
        return 1  # Base case: Only one way to move in a 1-row or 1-column grid
    return count_paths(x - 1, y) + count_paths(x, y - 1)

grid_size = 20
print(f"Number of routes in a {grid_size}×{grid_size} grid: {count_paths(grid_size, grid_size)}")
