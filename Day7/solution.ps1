# Advent of Code 2025 - Day 7
# Tachyon Beam Splitter - PowerShell Solution

# Read the grid from input file
$grid = Get-Content "input" | Where-Object { $_.Trim() -ne "" } | ForEach-Object { $_.Trim() }

$rows = $grid.Count
$cols = $grid[0].Length

# Find the starting position S
$startCol = $grid[0].IndexOf('S')

if ($startCol -eq -1) {
    Write-Host "Could not find starting position S!"
    exit
}

# Simulate tachyon beams
# Use a hashtable as a set to track active beam columns
$splitCount = 0
$activeBeams = @{ $startCol = $true }

# Process each row starting from row 1 (row after S)
for ($row = 1; $row -lt $rows; $row++) {
    $newBeams = @{}
    
    foreach ($col in $activeBeams.Keys) {
        # Check bounds
        if ($col -lt 0 -or $col -ge $cols) {
            continue
        }
        
        $ch = $grid[$row][$col]
        
        if ($ch -eq '^') {
            # Splitter! Count this split
            $splitCount++
            
            # New beams go left and right
            $leftCol = $col - 1
            $rightCol = $col + 1
            
            if ($leftCol -ge 0) {
                $newBeams[$leftCol] = $true
            }
            if ($rightCol -lt $cols) {
                $newBeams[$rightCol] = $true
            }
        } elseif ($ch -eq '.') {
            # Empty space, beam continues down
            $newBeams[$col] = $true
        }
    }
    
    $activeBeams = $newBeams
    
    # If no more active beams, we're done
    if ($activeBeams.Count -eq 0) {
        break
    }
}

Write-Host "Total number of splits: $splitCount"
