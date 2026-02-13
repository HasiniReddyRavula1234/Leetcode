class Solution {
    public int lengthOfLongestSubstring(String s) {
Map<Character, Integer> hm = new HashMap<>();
        int i = 0;
         int maxwin = 1;
         if(s.length() == 0)
         return 0;
        for(int j = 0;j < s.length();j++){
            char ch = s.charAt(j);
           int prevFreq = hm.getOrDefault(ch, 0);
            hm.put(ch,prevFreq + 1);

            // Invalid
            while(hm.get(ch) > 1){
                char ichar = s.charAt(i);
                hm.put(ichar, hm.get(ichar) - 1);
                i++;
            }
            maxwin = Math.max(maxwin, j - i + 1);
        }
        return maxwin;
    }
}