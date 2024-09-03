

void sect(float A[], float B[], float k, float C[])
{
    C[0] = (A[0] + k * B[0]) / (1 + k);
    C[1] = (A[1] + k * B[1]) / (1 + k);
}

