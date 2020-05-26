#include <math.h>
double doubles(int maxk, int maxn) {
    int k,n=0;
    double res=0;
    for ( k=1;k<=maxk;++k){
      for (n=1;n<=maxn;++n){
          res+=1/(k*pow(n+1,2*k));
      }
    }
    return res;
}
