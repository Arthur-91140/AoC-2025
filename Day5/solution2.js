const fs = require('fs');

// Lire le fichier input
const input = fs.readFileSync('input', 'utf8');
const lines = input.split(/\r?\n/);

const ranges = [];

for (const line of lines) {
    const trimmed = line.trim();

    // Ligne vide = fin des plages
    if (trimmed === '') {
        break;
    }

    // Parser une plage "start-end"
    const parts = trimmed.split('-');
    if (parts.length === 2) {
        const start = BigInt(parts[0]);
        const end = BigInt(parts[1]);
        ranges.push({ start, end });
    }
}

// Trier les plages par leur début
ranges.sort((a, b) => {
    if (a.start < b.start) return -1;
    if (a.start > b.start) return 1;
    return 0;
});

// Fusionner les plages qui se chevauchent
const merged = [];
for (const range of ranges) {
    if (merged.length === 0) {
        merged.push({ start: range.start, end: range.end });
    } else {
        const last = merged[merged.length - 1];
        // Si la plage actuelle chevauche ou touche la dernière plage fusionnée
        if (range.start <= last.end + 1n) {
            // Étendre la plage fusionnée si nécessaire
            if (range.end > last.end) {
                last.end = range.end;
            }
        } else {
            // Pas de chevauchement, ajouter comme nouvelle plage
            merged.push({ start: range.start, end: range.end });
        }
    }
}

// Compter le nombre total d'IDs frais
let totalFreshIds = 0n;
for (const range of merged) {
    // +1 car les bornes sont inclusives
    totalFreshIds += (range.end - range.start + 1n);
}

console.log(`Nombre de plages originales: ${ranges.length}`);
console.log(`Nombre de plages après fusion: ${merged.length}`);
console.log(`Nombre total d'IDs frais: ${totalFreshIds}`);
