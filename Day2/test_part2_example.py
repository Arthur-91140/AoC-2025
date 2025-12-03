def is_repeated_pattern_at_least_twice(n):
    """
    Check if a number is made of a sequence of digits repeated at least twice.
    """
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the total length is divisible by the pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            
            # Check for leading zeros
            if pattern[0] == '0':
                continue
            
            # Check if the entire string is made of this pattern repeated
            repetitions = length // pattern_len
            if repetitions >= 2:  # Must be repeated at least twice
                if pattern * repetitions == s:
                    return True
    
    return False

# Test with the example
test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

ranges = test_input.replace('\n', '').split(',')

total_sum = 0
all_invalid = []

print("Testing Part 2 with example:")
for range_str in ranges:
    range_str = range_str.strip()
    if not range_str:
        continue
    
    parts = range_str.split('-')
    if len(parts) != 2:
        continue
    
    start = int(parts[0])
    end = int(parts[1])
    
    invalid_ids = [n for n in range(start, end + 1) if is_repeated_pattern_at_least_twice(n)]
    
    if invalid_ids:
        print(f"Range {start}-{end}: {invalid_ids}")
        all_invalid.extend(invalid_ids)
        total_sum += sum(invalid_ids)

print(f"\nTotal sum: {total_sum}")
print(f"Expected: 4174379265")
print(f"Match: {total_sum == 4174379265}")
