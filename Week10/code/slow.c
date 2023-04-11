#include <stdlib.h>

#define SIZE_1 60000
#define SIZE_2 10000

int main(void) {
    int **mat = malloc(SIZE_1 * sizeof(int *));
    for (int i = 0; i < SIZE_1; ++i) {
        mat[i] = malloc(SIZE_2 * sizeof(int));
    }

    for (int i = 0; i < SIZE_2; ++i) {
        for (int j = 0; j < SIZE_1; ++j) {
            mat[j][i] = i * SIZE_2 + j;
        }
    }
    return 0;
}
