const fs = require('fs');

// Lire le fichier input
const input = fs.readFileSync('input', 'utf8');
const lines = input.split(/\r?\n/);

const ranges = [];
const ingredients = [];
let parsingRanges = true;

for (const line of lines) {
    const trimmed = line.trim();
    
    // Ligne vide = passage aux ingrédients
    if (trimmed === '') {
        parsingRanges = false;
        continue;
    }
    
    if (parsingRanges) {
        // Parser une plage "start-end"
        const parts = trimmed.split('-');
        if (parts.length === 2) {
            const start = BigInt(parts[0]);
            const end = BigInt(parts[1]);
            ranges.push({ start, end });
        }
    } else {
        // Parser un ID d'ingrédient
        const id = BigInt(trimmed);
        ingredients.push(id);
    }
}

// Vérifie si un ID est dans au moins une des plages
function isFresh(id, ranges) {
    for (const r of ranges) {
        if (id >= r.start && id <= r.end) {
            return true;
        }
    }
    return false;
}

// Compter les ingrédients frais
let freshCount = 0;
for (const id of ingredients) {
    if (isFresh(id, ranges)) {
        freshCount++;
    }
}

console.log(`Nombre de plages: ${ranges.length}`);
console.log(`Nombre d'ingrédients à vérifier: ${ingredients.length}`);
console.log(`Nombre d'ingrédients frais: ${freshCount}`);
