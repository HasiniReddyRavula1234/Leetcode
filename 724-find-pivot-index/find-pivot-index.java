class Solution {
    public int pivotIndex(int[] nums) {
        int ts = 0;
        int ls = 0,rs = 0;
        for(int i = 0;i < nums.length;i++){
            ts += nums[i];
        }
        for(int i = 0;i < nums.length;i++){
            rs = ts - ls - nums[i];
            if(ls == rs){
            return i;
        }
        ls = ls + nums[i];
        }
        return -1;




































    //   int[] prefix = new int[nums.length];
    //   prefix[0] = nums[0];
    //   int m = -1;
    //   int total = nums[0];
    //   for(int i = 1;i < nums.length;i++){
    //     total += nums[i];
    //     prefix[i] = nums[i] + prefix[i - 1];
    //           }  
    //   for(int i = 0;i < nums.length;i++){
    //     if(prefix[i] == total - prefix[i] + 1)
    //     m = i;
    //   }
    //   return m;
    }
}