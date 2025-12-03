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
    invalid_sum = 0  # Use running sum to avoid potential overflow issues
    
    for id_num in range(start, end + 1):
        if is_repeated_pattern(id_num):
            invalid_ids.append(id_num)
            invalid_sum += id_num
    
    return invalid_ids, invalid_sum

def solve(input_file):
    """Solve the invalid product ID problem."""
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # Parse the ranges - remove any newlines
    content = content.replace('\n', '')
    ranges = content.split(',')
    
    total_sum = 0
    range_count = 0
    
    for i, range_str in enumerate(ranges):
        range_str = range_str.strip()
        if not range_str:
            continue
        
        parts = range_str.split('-')
        if len(parts) != 2:
            continue
        
        try:
            start = int(parts[0])
            end = int(parts[1])
        except ValueError:
            continue
        
        invalid_ids, range_sum = find_invalid_ids_in_range(start, end)
        
        if invalid_ids:
            print(f"Range {start:12d}-{end:12d}: {len(invalid_ids):4d} invalid IDs, sum = {range_sum:15d}")
            total_sum += range_sum
            range_count += 1
        else:
            print(f"Range {start:12d}-{end:12d}:    0 invalid IDs")
    
    print(f"\n{'='*70}")
    print(f"Ranges with invalid IDs: {range_count}")
    print(f"Total sum: {total_sum}")
    print(f"{'='*70}")
    
    return total_sum

if __name__ == "__main__":
    input_file = r"c:\Users\tutur\Desktop\fichier divers\AoC-2025\Day2\input"
    result = solve(input_file)
    print(f"\nFinal Answer: {result}")
