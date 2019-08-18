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