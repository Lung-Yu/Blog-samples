/* leetcode_8_String to Integer (atoi)*/

class Solution {
    public int myAtoi(String str) {
        int Init = 0 , valid_size = 10 , isPositive = -1,unit = 10 , num_count = 0;
        long sum = 0;
        
        for(int i=0;i<str.length();i++){
            char temp = str.charAt(i);
            
            if((temp-48) <= 9 && (temp-48) >= 0) {
                sum = (temp-48) + (sum*unit);    
                Init = 1;
                num_count++;
            }else if((temp - '+') ==0){
                if(isPositive != -1)    return 0;
                isPositive = 1;
                Init = 1;
            }else if((temp - '-') == 0){
                if(isPositive != -1)    return 0;
                isPositive = 0; // false
                Init = 1;
            }else if(Init == 1){
                break;
            }else if((temp - ' ') == 0){
                valid_size++;
            }else{
                break;
            }
            
        }
        
        if(isPositive == 0)
            sum *= -1;

        
        if(num_count >11 && isPositive == 0)
            return -2147483648;
        else if(num_count >11)
            return 2147483647;
        else if(sum > 2147483647)
            return 2147483647;
        else if(sum < -2147483648 )
            return -2147483648;
        else
            return (int)sum;
    }
}