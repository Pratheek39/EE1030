
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void transpose(int n,double** matrix){
	for(int i = 0 ; i < n ; i++){
		for(int j = i+1 ; j < n ;j++){
			double temp = matrix[i][j];
			matrix[i][j] = matrix[j][i];
			matrix[j][i] = temp;
		}
	}

}
void assign(int m,int n,double** mat,double** new){
	for(int i = 0; i < m ;i++){
		for(int j = 0 ; j < n ;j++){
			new[i][j] = mat[i][j];
		}
	}
}
double norm(double* vec,int n){
	double sum = 0;
	for(int i = 0 ; i < n ; i++){
		sum += vec[i]*vec[i];
	}
	return sqrt(sum);
}
double dot(double* vec1,double* vec2,int n){
	double sum = 0;
	for(int i = 0 ; i < n ; i++){
		sum += vec1[i]*vec2[i];
	}
	return sum;
}
void matmul(int n,double** R,double** Q,double** mat){
	transpose(n,Q);
	for(int i = 0 ; i < n ; i++){
		for(int j = 0 ; j < n ; j++){
			mat[i][j] = dot(R[i],Q[j],n);
		}
	}
	transpose(n,Q);
}

// Removes vec2 from vec1
void removeProjection(double* vec1,double* vec2,int n ){
	double p = dot(vec1,vec2,n)/dot(vec2,vec2,n);
	
	for(int i = 0 ; i < n ; i++){
		vec1[i] = vec1[i] - p*vec2[i];
	}
	
}
//Finds Q using Gram-scmidt process.
void findQ(int n,double** mat,double** Q){
	assign(n,n,mat,Q);

	transpose(n,Q);
	for(int i = 0 ; i < n ; i++){
		
		for(int j = 0 ; j < i ; j++ ){
			removeProjection(Q[i],Q[j],n);
				}
	}
	for(int i = 0 ; i < n ; i++){
		double p = norm(Q[i],n);
		for(int j = 0 ; j < n ;j++){
			Q[i][j] = Q[i][j]/p;
		}
	}
	transpose(n,Q);
}

double calculateDiff(int n,double** mat,double** new){
	double diff = 0;
	for(int i = 0 ; i < n ; i++){
		diff += fabs(mat[i][i]-new[i][i]);
	}
	return diff;
}
void printmatrix(int n, double** matrix){
	for(int i = 0 ; i < n ;i++){
		for(int j = 0 ; j < n ; j++){
			printf("%.10lf ",matrix[i][j]);
		}
		printf("\n");
	}
}
//Function to find the eigenvalues
int FindEigenValues(int n,double** mat,double** Q){
	double** newPtr1 = malloc(n*sizeof(double*));
	double** newPtr2 = malloc(n*sizeof(double*));

	for(int i = 0 ; i < n ; i++){
		newPtr1[i] = malloc(n*sizeof(double)); 
		newPtr2[i] = malloc(n*sizeof(double)); 
	}
	double diff;
	assign(n,n,mat,newPtr1);
	assign(n,n,mat,newPtr2);
	findQ(n,mat,Q);
	matmul(n,mat,Q,newPtr1);
	transpose(n,Q);
	matmul(n,Q,newPtr1,mat);
	int it = 1;
	
	diff = calculateDiff(n,mat,newPtr2);
	long double x= pow(10,-10);
	while(diff > x ){
		assign(n,n,mat,newPtr1);
		assign(n,n,mat,newPtr2);
		findQ(n,mat,Q);

		matmul(n,mat,Q,newPtr1);
		transpose(n,Q);
		matmul(n,Q,newPtr1,mat);

		diff = calculateDiff(n,mat,newPtr2);
		it++;
		if(it>10000){
		printf("too many iterations!");
		return it;
		}

	}
	printf("The eigenvalues are:\n");
	
	for(int i = 0 ; i < n ; i++){
		printf("%lf ",isnan(mat[i][i])?0:mat[i][i]);
	}
	printf("\n");


	return it;
	
}




// A function to fill the aditional entries with ones and zeros.
double** fillMatrix(double** mat , int m , int n){

    double** Ptr = malloc(n*sizeof(double*));
    for (int i = 0; i < n; i++){
        Ptr[i] = malloc(n*sizeof(double));
        for(int j = 0 ; j < n ; j++){
            if(j>=n-m && i>=n-m){
                Ptr[i][j] = mat[i+m-n][j+m-n];
            }
            else{
                if(j==i)Ptr[i][j] = 1;
                else Ptr[i][j] = 0;
            }
        }
    }
    
    return Ptr;
    
}
// Builds the HouseHolder matrix for reflection i.e. (I - 2u*u^T)
double** houseHolder(double* vec1,double* vec2,int n){
    
    double* u = malloc(n*sizeof(double));
    for(int i = 0 ; i < n; i++){
        u[i] = (vec2[i] - vec1[i]);
    }
    double p = norm(u,n);
    for(int i = 0 ; i < n ; i++){
        u[i] = u[i]/p;
    }
    double** Ptr = malloc(n*sizeof(double*));
    for(int i = 0 ; i < n ; i++){
        Ptr[i] = malloc(n*sizeof(double));
        for (int j = 0; j < n; j++){
            if(i==j)Ptr[i][j] = 1 - 2*u[i]*u[i];
            else Ptr[i][j] = -2*u[i]*u[j];
        }
        
    }
    free(u);
    return Ptr;
   

}






//uses the householder reflection and converts a given matrix to a hessenberg matrix that is similar to it.
double** makeHessenberg(double** mat,int n){
   
    
    
    double** new = malloc(n*sizeof(double*));
    for(int i = 0 ; i < n ; i++){
        new[i] = malloc(n*sizeof(double));
    }
    
    for(int i = 0 ; i < n-1 ; i++){
     
        double* vec1 = malloc((n-i-1)*sizeof(double));
        double* vec2 = malloc((n-i-1)*sizeof(double));
      
        for(int j = 0 ; j < n-i-1; j++){
            vec1[j] = mat[j+i+1][i];
        }
		double len = norm(vec1,n-i-1);
		if(len == 0)continue;
        if(vec1[0]<0)vec2[0] = len;
        else vec2[0] = -1*len;

        for(int j = 1 ; j < n-i-1; j++){
            vec2[j] = 0;
        }
        double** hPtr = houseHolder(vec1,vec2,n-i-1);
        double** newPtr = fillMatrix(hPtr,n-i-1,n);
        
         matmul(n,newPtr,mat,new);
         matmul(n,new,newPtr,mat);
        for (int j = 0; j < n-i-1; j++) {
            free(hPtr[j]);
        }
        free(hPtr);
        for (int j = 0; j < n; j++) {
            free(newPtr[j]);
        }
        free(newPtr);
            free(vec1);
            free(vec2);
        
            

    }
    
    
    
    return mat;
}




int main(){
	int n;
	scanf("%d",&n);
	double** matrix = malloc(n*sizeof(double*));
	
	double** Q = malloc(n*sizeof(double*));
	
	for(int i = 0 ; i < n ; i++){
		matrix[i] = malloc(n*sizeof(double));
		for(int j = 0 ;  j < n ; j++){
			scanf("%lf",&matrix[i][j]);
		}
	}
	
	for(int i = 0 ; i < n ; i++){
		
		Q[i] = malloc(n*sizeof(double));
		for(int j = 0 ; j < n ; j++){
			
			Q[i][j] = 0;
		}
	}
	 double** newMatrix = makeHessenberg(matrix,n);
	// printmatrix(n,newMatrix);
	 //return 0;
	int i = eig(n,newMatrix,Q);
	printf("Number of iterations in the QR Algorithm: %d",i);
}
