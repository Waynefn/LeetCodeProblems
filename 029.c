int divide(int divdend, int divisor) {
    unsigned int divdu=divdend;
    unsigned int divsu=divisor;
    if(divsu==0 || divdend==-2147483648 && divsu==-1)return 0x7fffffff;
    int sign=1;
    if(divdend<0){
        divdu=-divdend;
        sign=-sign;
    }
    if(divisor<0){
        divsu=-divisor;
        sign=-sign;
    }
    if(divdu<divsu)return 0;
    int result=0;
    int t=0;
    for(int i=31;i>=0;i--){
        int ibit=((1<<i)&divdu)>>i;
        t=(t<<1)+ibit;
        if(t>=divsu){
            t-=divsu;
            result=(result<<1)+1;
        }
        else result=result<<1;
    }
    if(sign<0)return -result;
    return result;
}
