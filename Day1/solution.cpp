#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream inputFile("input");
    
    if (!inputFile.is_open()) {
        cerr << "Erreur: impossible d'ouvrir le fichier input" << endl;
        return 1;
    }
    
    int position = 50;  // Le cadran démarre à 50
    int count = 0;      // Nombre de fois où le cadran pointe sur 0
    
    string line;
    while (getline(inputFile, line)) {
        if (line.empty()) continue;
        
        char direction = line[0];  // 'L' ou 'R'
        int distance = stoi(line.substr(1));  // La distance numérique
        
        // Appliquer la rotation
        if (direction == 'L') {
            position = (position - distance) % 100;
            if (position < 0) position += 100;
        } else if (direction == 'R') {
            position = (position + distance) % 100;
        }
        
        // Vérifier si on pointe sur 0
        if (position == 0) {
            count++;
        }
    }
    
    inputFile.close();
    
    cout << "Le mot de passe est: " << count << endl;
    
    return 0;
}
