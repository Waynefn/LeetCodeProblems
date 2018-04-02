class Solution {
    public String convert(String s, int numRows) {
	    if(numRows==1)return new String(s);
    	char[] ch=new char[s.length()+5];
    	int k=0;int i=0;
    	int gap=2*numRows-2;
    	int t=gap;
    	while(i<s.length()) {
    		ch[k++]=s.charAt(i);
    		i=i+gap;
    	}
    	for(int line=1;line<numRows-1;line++) {
    		i=line;
    		t-=2;
        	while(i<s.length()) {
        		ch[k++]=s.charAt(i);
        		if(i+t<s.length())
        			ch[k++]=s.charAt(i+t);
        		i=i+gap;
        	}
    	}
    	i=numRows-1;
    	while(i<s.length()) {
    		ch[k++]=s.charAt(i);
    		i=i+gap;
    	}
    	return new String(ch).trim();
    }
}
