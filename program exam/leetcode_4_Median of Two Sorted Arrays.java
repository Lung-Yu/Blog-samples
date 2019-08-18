/* leetcode_4_Median of Two Sorted Arrays */

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int size = nums1Size + nums2Size;
    int idx_median = size / 2;
    int *res_array = malloc(sizeof(int) * size);
    int i=0,j=0;
    double median_num = 0;
    
    while(i+j < size){
        if(i == nums1Size)
            res_array[(i+j)] = nums2[j++];
        else if(j == nums2Size)
            res_array[(i+j)] = nums1[i++];
        else if(nums1[i] < nums2[j])
            res_array[(i+j)] = nums1[i++];
        else
            res_array[(i+j)] = nums2[j++];
    }
    
    if(size % 2 == 0)
        median_num = ((double)res_array[idx_median] + (double)res_array[(idx_median-1)]) / 2;
    else
        median_num = res_array[idx_median];

    return median_num;
}