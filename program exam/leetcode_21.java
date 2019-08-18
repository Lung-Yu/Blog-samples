/* leetcode_21_Merge Two Sorted Lists */

import java.util.Collections;
import java.util.List;
import java.util.LinkedList;


public class leetcode_21{

    public static void main(String[] args){
        ListNode n11 = new ListNode(1);
        ListNode n12 = new ListNode(1);
        n11.next = n12;
        ListNode n13 = new ListNode(1);
        n12.next = n13;

        ListNode n21 = new ListNode(1);
        ListNode n22 = new ListNode(1);
        n21.next = n22;
        ListNode n23 = new ListNode(1);
        n22.next = n23;
        
        mergeTwoLists(n11,n21);

    }

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        List<Integer> list = sort(l1,l2);
        ListNode res = null;
    
        for (int i : list){
            ListNode node = new ListNode(i);
            node.next = res;
            res = node;
        }
        
        return res;
    }

    private static List<Integer> sort(ListNode l1, ListNode l2){
        List<Integer> list = new LinkedList<Integer>();
        
        while(l1!=null){
            list.add(l1.val);
            l1 = l1.next;
        }

        while(l2!=null){
            list.add(l2.val);
            l2 = l2.next;
        }

        Collections.sort(list,Collections.reverseOrder());  
        return list;
    }

}

class ListNode{
    public int val;
    public ListNode next;
    public ListNode(int val){
        this.val = val;
    }
}
