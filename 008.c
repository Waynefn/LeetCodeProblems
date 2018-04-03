inline int isNum(char i){
    return(i>='0' && i<='9');
}


int myAtoi(char* str) {
    int i=0;
    int num=0;
    int sign=0;
    while(str[i]!='\0'){
        if(str[i]=='-' || str[i]=='+'){
            if(sign==0)sign=str[i];
            else return 0;
        }
        else if (str[i]==' ' && sign==0);
        else if(isNum(str[i])) break;
        else return 0;
        ++i;
    }
    while(str[i]!='\0'){
        if(isNum(str[i])){
            if(num<=INT_MAX/10)
            num=num*10+(str[i]-'0');
            else {
                num=-1;
                break;
            }
          }
        else break;
        ++i;
    }
    if(sign=='-'){
        if(num<0)return INT_MIN;
        else return -num;
    }
    else{
        if(num<0)return INT_MAX;
        else return num;
    }
}
