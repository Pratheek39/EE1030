#include <math.h>
#include <stdlib.h>

typedef struct {
    double x;
    double y;
    double z;
} Vector;

// Function to calculate the direction cosines of the line joining two points
Vector* calculate_cosines(double x1, double y1, double z1, double x2, double y2, double z2) {
    Vector* result = (Vector*)malloc(sizeof(Vector));

    // Calculate the direction vector
    double dx = x2 - x1;
    double dy = y2 - y1;
    double dz = z2 - z1;

    // Calculate the magnitude of the direction vector
    double magnitude = sqrt(dx * dx + dy * dy + dz * dz);

    // Calculate direction cosines
    result->x = dx / magnitude;  // cos(alpha)
    result->y = dy / magnitude;  // cos(beta)
    result->z = dz / magnitude;  // cos(gamma)

    return result;
}

// Function to free the allocated vector
void free_vector(Vector* vec) {
    free(vec);
}

