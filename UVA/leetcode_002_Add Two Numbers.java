class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum = 0,unit = 1;
        ArrayList<Integer> array = new ArrayList<Integer>(); 
        while(l1!=null || l2!=null){
            if(l1!=null){
                sum += l1.val * unit;
                l1 = l1.next;
            }
            if(l2!=null){
                sum += l2.val * unit;
                l2 = l2.next;
            }
            array.add(sum%10);
            sum /= 10;
        }
    
        while(sum > 0){
            array.add(sum%10);
            sum /= 10;
        }
        
        Collections.reverse(array);
        
        ListNode node =null;
        for(int v : array){
            System.out.println(v);
            ListNode temp = new ListNode(v);
            temp.next = node;
            node = temp;
        }
       
        
        return node;
    }
}