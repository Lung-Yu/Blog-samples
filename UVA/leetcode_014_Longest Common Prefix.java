public static String longestCommonPrefix(String[] strs) {
	if(strs.length == 0)
		return "";
	
	String res = strs[0];
	
	for(int i=1;i<strs.length;i++){
		String tempStr = strs[i];
		int min_size = tempStr.length() > res.length() ? res.length() : tempStr.length();
		res= res.substring(0,min_size);
		for(int j=0;j<min_size;j++){
			if(tempStr.charAt(j)!= res.charAt(j)){
				
				res = res.substring(0, j);
				break;
			}
		}
	}
	return res;
}