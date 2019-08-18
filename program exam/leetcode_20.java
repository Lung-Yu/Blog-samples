/* leetcode_20_Valid Parentheses */

import java.util.Stack;

public class leetcode_20{

    public static void main(String[] args){
        System.out.println(isValid("]()((){"));
        System.out.println(isValid("[()(()){([]())}]"));
        
    }

    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        if(s.length()%2!=0)
            return false;
    
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            
            if(c == '(')
                stack.push(')');
            else if(c == '[')
                stack.push(']');
           else if(c == '{')
               stack.push('}');
           else{
               if(stack.isEmpty())
                   return false;
               
               char t = stack.pop();
               if(t != c)
                   return false;
           }
        
       }
       if(stack.empty())
            return true;
       else
            return false;
    }
}
