#include <stdio.h>

int main(int argc, char* argv[]){
  printf("n = ");
  int n;

  /*TODO: Read in n from the user */
  scanf("%d", &n);
  unsigned int denom = 1;
  double e = 1;

  for(int i = 1; i <= n; i++){
    /* TODO: Update denom, update the sum */
    denom = fact(i);
    e += 1.0 / denom;
  }
  printf("e =  %lf\n", e);
  return 0;
}
int fact(int n) {
    int ans = 1;
    for (int i = 2; i <= n; ++i)
        ans *= i;
    return ans;
}
