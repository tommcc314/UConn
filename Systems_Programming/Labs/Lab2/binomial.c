/* Implementing a binomial */

#include <stdio.h>

int binomial(int n, int k){
    /*
        TODO: Fill this function in. Reminder, it's recursive. 
    */
    if (k == 0 || k == n) return 1;
    return binomial(n - 1, k) + binomial(n - 1, k - 1);
}

int main(int argc, char* argv[]){
    int n, k;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Enter k: ");
    scanf("%d", &k);
    printf("%d choose %d = %d\n", n, k, binomial(n, k));

    return 0;
}
