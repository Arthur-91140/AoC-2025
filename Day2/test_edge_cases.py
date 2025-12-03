def is_repeated_pattern(n):
    """
    Check if a number is made of a sequence of digits repeated exactly twice.
    Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    No leading zeros allowed.
    """
    s = str(n)
    length = len(s)
    
    # Must be even length to be repeated twice
    if length % 2 != 0:
        return False
    
    # Split in half
    half = length // 2
    first_half = s[:half]
    second_half = s[half:]
    
    # Check if both halves are identical and no leading zeros
    if first_half == second_half and first_half[0] != '0':
        return True
    
    return False

# Let me test some edge cases manually
test_cases = [
    (11, True),
    (22, True),
    (99, True),
    (1010, True),
    (101, False),  # odd length
    (1001, False),  # 10 != 01
    (1188511885, True),  # 11885 + 11885
    (222222, True),  # 222 + 222
    (446446, True),  # 446 + 446
    (38593859, True),  # 3859 + 3859
    (123123, True),  # 123 + 123
    (565656, False),  # 565 != 656
]

print("Testing edge cases:")
for num, expected in test_cases:
    result = is_repeated_pattern(num)
    status = "✓" if result == expected else "✗"
    print(f"{status} {num}: {result} (expected {expected})")
    if result != expected:
        s = str(num)
        if len(s) % 2 == 0:
            half = len(s) // 2
            print(f"   '{s[:half]}' vs '{s[half:]}'")
