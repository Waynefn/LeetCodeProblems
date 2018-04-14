int removeDuplicates(int* nums, int numsSize) {
    if(nums==NULL || numsSize==0)return 0;
    int nlen=1;
    int last=*nums;
    for(int i=1;i<numsSize;i++){
        if(nums[i]!=last){
            nums[nlen]=nums[i];
            last=nums[nlen++];
        }
          
    }
    return nlen;
}
