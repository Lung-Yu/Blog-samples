/* leetcode_9_Palindrome Number */
public class leetcode_9{
    public static void main(String[] args){
        System.out.println(isPalindrome(1001));
        System.out.println(isPalindrome(-1150));
    }

    public static boolean isPalindrome(int x) {
        if(x<0) return false;
        String s = String.valueOf(x);

        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1))
                return false;
        }
        return true;
    }
}
