#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 150
#define MAX_COLS 150

// Count adjacent rolls for a position
int count_adjacent(char grid[MAX_ROWS][MAX_COLS], int rows, int cols, int i,
                   int j) {
  // 8 directions: N, NE, E, SE, S, SW, W, NW
  int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
  int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};

  int count = 0;
  for (int d = 0; d < 8; d++) {
    int ni = i + dx[d];
    int nj = j + dy[d];

    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
      if (grid[ni][nj] == '@') {
        count++;
      }
    }
  }
  return count;
}

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
    while (len > 0 &&
           (grid[rows][len - 1] == '\n' || grid[rows][len - 1] == '\r')) {
      grid[rows][len - 1] = '\0';
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

  int total_removed = 0;
  int iteration = 0;

  // Keep removing until no more rolls can be removed
  while (1) {
    // Find all rolls that can be removed (< 4 adjacent)
    int to_remove[MAX_ROWS][MAX_COLS] = {0};
    int removable_count = 0;

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (grid[i][j] == '@') {
          int adjacent = count_adjacent(grid, rows, cols, i, j);
          if (adjacent < 4) {
            to_remove[i][j] = 1;
            removable_count++;
          }
        }
      }
    }

    // If nothing can be removed, we're done
    if (removable_count == 0) {
      break;
    }

    // Remove all marked rolls
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (to_remove[i][j]) {
          grid[i][j] = '.';
        }
      }
    }

    iteration++;
    total_removed += removable_count;
    printf("Iteration %d: removed %d rolls\n", iteration, removable_count);
  }

  printf("\nTotal rolls removed: %d\n", total_removed);

  return 0;
}
