def find_max_joltage(bank):
    """Find the maximum joltage possible from a battery bank."""
    max_joltage = 0
    
    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the two-digit number
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def solve(input_file):
    """Solve the battery joltage problem."""
    total_joltage = 0
    
    with open(input_file, 'r') as f:
        for line in f:
            bank = line.strip()
            if bank:  # Skip empty lines
                max_jolt = find_max_joltage(bank)
                total_joltage += max_jolt
                print(f"Bank: {bank[:20]}{'...' if len(bank) > 20 else ''} -> Max joltage: {max_jolt}")
    
    return total_joltage

if __name__ == "__main__":
    input_file = r"c:\Users\tutur\Desktop\fichier divers\AoC-2025\Day3\input"
    result = solve(input_file)
    print(f"\nTotal output joltage: {result}")
