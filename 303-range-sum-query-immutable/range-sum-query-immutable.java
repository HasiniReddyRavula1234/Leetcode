class NumArray {
    int[] prefix;
    public NumArray(int[] nums) {
    prefix = new int[nums.length];
        prefix[0] = nums[0];
        for(int i = 1;i < nums.length;i++){
            prefix[i] = nums[i] + prefix[i-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             1];
        }

    }
    
    public int sumRange(int left, int right) {
        int p = 0;
        if(left == 0)
        p = prefix[right];
        else{
            p = prefix[right] - prefix[left - 1];
        }
        return p;
    }
}
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */