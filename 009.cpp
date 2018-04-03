class Solution {
public:
    inline int getLength(int x){
        double j=1;
        while(j*10-1<x)
            j*=10;
        return (int)j;
    }
    bool isPalindrome(int x) {
        if(x<10 && x>=0)return true;
        else if (x<0)return false;
        int i=10;
        int j=getLength(x);
        while(j>=i){
            if(x/j%10!=x%i/(i/10))return false;
            j/=10;
            i*=10;
        }
        return true;
    }
};
