double myPow(double x, int y) {
    double res=1;
    unsigned int n;
    if(y<0){
        x=1/x;
        n=-y;
    }else
        n=y;
    
    while(n>0){
        if(n%2==1)
            res*=x;
        n/=2;
        x*=x;
    }
    return res;
}
