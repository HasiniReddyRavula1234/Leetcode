class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int min_diff = Integer.MAX_VALUE;
        char ch = letters[0];
        for(int i = 0;i < letters.length;i++){
            if((int)letters[i] > (int)target && letters[i] - target < min_diff){
            min_diff =  (int)letters[i] - (int)target;
            ch = letters[i];
            }
        }
        return ch;
    }
}