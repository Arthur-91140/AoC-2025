def is_repeated_pattern(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    first_half = s[:half]
    second_half = s[half:]
    return first_half == second_half and first_half[0] != '0'

# Test range 25-39 which should have 33
result = [n for n in range(25, 40) if is_repeated_pattern(n)]
print(f"Invalid IDs in 25-39: {result}")
print(f"Sum: {sum(result)}")
print(f"Expected: 33")
