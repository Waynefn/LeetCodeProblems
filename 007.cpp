int reverse(int x) {
    int flag=(x>0)?1:-1;
    x*=flag;
    int ret=0;
    while(x>0){
        if(ret>214748364)return 0;
        int r=x%10;
        x=(x-r)/10;
        ret=ret*10+r;     
    }
    return flag*ret;
}
