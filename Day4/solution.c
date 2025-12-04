#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 150
#define MAX_COLS 150

int main() {
    FILE *file = fopen("input", "r");
    if (!file) {
        printf("Error opening file\n");
        return 1;
    }
    
    char grid[MAX_ROWS][MAX_COLS];
    int rows = 0;
    int cols = 0;
    
    // Read the grid
    while (fgets(grid[rows], MAX_COLS, file)) {
        // Remove newline/carriage return
        int len = strlen(grid[rows]);
        while (len > 0 && (grid[rows][len-1] == '\n' || grid[rows][len-1] == '\r')) {
            grid[rows][len-1] = '\0';
            len--;
        }
        
        if (len > 0) {
            if (cols == 0) {
                cols = len;
            }
            rows++;
        }
    }
    fclose(file);
    
    printf("Grid size: %d x %d\n", rows, cols);
    
    // Count accessible rolls
    int accessible = 0;
    
    // 8 directions: N, NE, E, SE, S, SW, W, NW
    int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
    int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '@') {
                // Count adjacent rolls
                int adjacent_count = 0;
                
                for (int d = 0; d < 8; d++) {
                    int ni = i + dx[d];
                    int nj = j + dy[d];
                    
                    // Check bounds
                    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                        if (grid[ni][nj] == '@') {
                            adjacent_count++;
                        }
                    }
                }
                
                // If fewer than 4 adjacent rolls, it's accessible
                if (adjacent_count < 4) {
                    accessible++;
                }
            }
        }
    }
    
    printf("Rolls accessible by forklift: %d\n", accessible);
    
    return 0;
}
