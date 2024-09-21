#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    double x;
    double y;
    double z;
} Vector;

__attribute__((visibility("default"))) Vector* calculate_cosines(double px, double py, double pz, double qx, double qy, double qz) {
    // Calculate direction vector PQ
    double dx = qx - px;
    double dy = qy - py;
    double dz = qz - pz;

    // Calculate magnitude
    double magnitude = sqrt(dx * dx + dy * dy + dz * dz);

    // Allocate memory for the result
    Vector* result = (Vector*)malloc(sizeof(Vector));
    if (!result) {
        return NULL; // Handle memory allocation failure
    }

    // Calculate direction cosines
    result->x = dx / magnitude; // Cosine alpha
    result->y = dy / magnitude; // Cosine beta
    result->z = dz / magnitude; // Cosine gamma

    return result;
}

__attribute__((visibility("default"))) void free_vector(Vector* vec) {
    free(vec);
}

