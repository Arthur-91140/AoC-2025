# Advent of Code 2025 - Day 7 Part 2
# PowerShell

param([string]$InputFile = "input")

$lignes = Get-Content $InputFile
$splitters = @{}
$start = $null
$pmax = 0

for ($i = 0; $i -lt $lignes.Count; $i++) {
    for ($j = 0; $j -lt $lignes[$i].Length; $j++) {
        $char = $lignes[$i][$j]
        if ($char -eq '^') {
            $splitters["$i,$j"] = $true
            if ($i -gt $pmax) { $pmax = $i }
        }
        if ($char -eq 'S') {
            $start = @($i, $j)
        }
    }
}

# Memoization cache
$cache = @{}

function nbtimelines($p, $q) {
    $key = "$p,$q"
    if ($cache.ContainsKey($key)) { return $cache[$key] }
    
    if ($p -gt $script:pmax) {
        return [bigint]1
    }
    
    if (-not $script:splitters.ContainsKey($key)) {
        # Pas un splitter, on descend
        $result = nbtimelines ($p + 1) $q
    } else {
        # C'est un splitter, on va a gauche ET a droite (meme ligne)
        $result = (nbtimelines $p ($q - 1)) + (nbtimelines $p ($q + 1))
    }
    
    $cache[$key] = $result
    return $result
}

$result = nbtimelines $start[0] $start[1]
Write-Host "Part 2 : $result"
