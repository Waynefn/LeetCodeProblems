int strStr(char* haystack, char* needle) {
    if(haystack[0]=='\0' && needle[0]=='\0')return 0;
    int s1,s2,ret;    
    s2=0;
    for(s1=0;haystack[s1]!='\0';s1=ret+1){
        ret=s1;
        while(1){
         if(needle[s2]=='\0')
             return ret;
         if(haystack[s1++]!=needle[s2++])
             break;
        }
        s2=0;
    }
    return -1;
}
