void direction_cosines(float x1, float y1, float z1, float x2, float y2, float z2, float *l, float *m, float *n) {
       float dx = x2 - x1;
    float dy = y2 - y1;
    float dz = z2 - z1;

       float magnitude = sqrt(dx*dx + dy*dy + dz*dz);

    
    *l = dx / magnitude;
    *m = dy / magnitude;
    *n = dz / magnitude;
}
