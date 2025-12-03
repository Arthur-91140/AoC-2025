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

def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs in the given range [start, end]."""
    invalid_ids = []
    
    for id_num in range(start, end + 1):
        if is_repeated_pattern(id_num):
            invalid_ids.append(id_num)
    
    return invalid_ids

# Test with the example
test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

ranges = test_input.replace('\n', '').split(',')

total_sum = 0
all_invalid = []

print("Testing with example:")
for range_str in ranges:
    range_str = range_str.strip()
    if not range_str:
        continue
    
    parts = range_str.split('-')
    if len(parts) != 2:
        continue
    
    start = int(parts[0])
    end = int(parts[1])
    
    invalid_ids = find_invalid_ids_in_range(start, end)
    
    if invalid_ids:
        print(f"Range {start}-{end}: {invalid_ids}")
        all_invalid.extend(invalid_ids)
        total_sum += sum(invalid_ids)

print(f"\nTotal sum: {total_sum}")
print(f"Expected: 1227775554")
print(f"Match: {total_sum == 1227775554}")
