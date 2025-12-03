def is_repeated_pattern_at_least_twice(n):
    """
    Check if a number is made of a sequence of digits repeated at least twice.
    Examples: 
    - 111 (1 three times)
    - 123123 (123 two times)
    - 565656 (56 three times)
    - 1212121212 (12 five times)
    No leading zeros allowed.
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

def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs in the given range [start, end]."""
    invalid_ids = []
    invalid_sum = 0
    
    for id_num in range(start, end + 1):
        if is_repeated_pattern_at_least_twice(id_num):
            invalid_ids.append(id_num)
            invalid_sum += id_num
    
    return invalid_ids, invalid_sum

def solve_part2(input_file):
    """Solve the invalid product ID problem for part 2."""
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
    
    print(f"\n{'='*70}")
    print(f"Ranges with invalid IDs: {range_count}")
    print(f"Total sum: {total_sum}")
    print(f"{'='*70}")
    
    return total_sum

if __name__ == "__main__":
    input_file = r"c:\Users\tutur\Desktop\fichier divers\AoC-2025\Day2\input"
    result = solve_part2(input_file)
    print(f"\nFinal Answer: {result}")
