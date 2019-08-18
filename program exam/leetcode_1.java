/* leetcode_1_Two Sum */

public class leetcode_1 {
    public static void main(String[] args){
        
        for(int item : twoSum(new int[]{11,55,21,2,5,2},7))
            System.out.println(item);
    }
    public static int[] twoSum(int[] nums, int target) {
        
        for(int i = 0;i < nums.length ; i++){
            for(int j=i+1 ; j<nums.length;j++){
                if(nums[i] + nums[j] == target)
                    return new int[]{i,j};
            }
        }
        return new int[]{0,0};
    }
}
