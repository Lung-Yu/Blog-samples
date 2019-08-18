#define MIN(a,b) (((a)<(b))?(a):(b))

int removeElement(int* nums, int numsSize, int val) {
    int i = 0,j;
    int count = 0;
    int idx = 0;
    int end = numsSize;
    for(i=0 ; i< end; i++){
    	if(nums[i]==val){
            for(j=i;j<(end-1);j++){
                nums[j]=nums[j+1];
            }  
            end--;
            i--;
        }else{
            count++;
        } 
    }
    
    return count;
}