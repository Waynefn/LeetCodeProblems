char* longestCommonPrefix(char** strs, int strsSize) {
    char*ret=(char*)calloc(500,sizeof(char));
    if(strs==NULL || strs[0]==NULL)return ret;
    for(int i=0;strs[0][i]!='\0';i++){
        for(int j=0;j<strsSize;j++){
            if(strs[j][i]!=strs[0][i])
                return ret;  
        }
        ret[i]=strs[0][i];
    }
    return ret;
}
