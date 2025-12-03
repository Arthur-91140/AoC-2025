def find_max_joltage_12(bank):
    """
    Find the maximum joltage possible from a battery bank by selecting exactly 12 batteries.
    Uses a greedy algorithm: for each position in the result, pick the largest digit
    that still leaves enough digits to complete the 12-digit number.
    """
    n = len(bank)
    k = 12  # Number of batteries to select
    
    if n < k:
        return 0  # Not enough batteries
    
    result = []
    current_pos = 0
    
    for i in range(k):
        # How many more digits do we need after this one?
        remaining = k - i - 1
        
        # We can search from current_pos to (n - remaining)
        # This ensures we have enough digits left to select
        search_end = n - remaining
        
        # Find the maximum digit in this range
        max_digit = '0'
        max_pos = current_pos
        
        for j in range(current_pos, search_end):
            if bank[j] > max_digit:
                max_digit = bank[j]
                max_pos = j
        
        result.append(max_digit)
        current_pos = max_pos + 1
    
    return int(''.join(result))

def solve_part2(input_file):
    """Solve the battery joltage problem for part 2."""
    total_joltage = 0
    
    with open(input_file, 'r') as f:
        for line in f:
            bank = line.strip()
            if bank:  # Skip empty lines
                max_jolt = find_max_joltage_12(bank)
                total_joltage += max_jolt
                print(f"Bank: {bank[:20]}{'...' if len(bank) > 20 else ''} -> Max joltage: {max_jolt}")
    
    return total_joltage

if __name__ == "__main__":
    input_file = r"c:\Users\tutur\Desktop\fichier divers\AoC-2025\Day3\input"
    result = solve_part2(input_file)
    print(f"\nTotal output joltage: {result}")
