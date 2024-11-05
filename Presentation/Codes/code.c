#include <math.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    double x;
    double y;
    double z;
} Vector;

// Function to calculate the direction cosines of the line joining two points
Vector* calculate_cosines(Vector* P, Vector* Q) {
    Vector* result = (Vector*)malloc(sizeof(Vector));

    // Calculate the direction vector
    double dx = Q->x - P->x;
    double dy = Q->y - P->y;
    double dz = Q->z - P->z;

   
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

