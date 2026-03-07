class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length + nums2.length;
        int[] nums = new int[n];
        int count = 0;
        for(int i = 0;i < nums1.length;i++){
            nums[count++] = nums1[i];
            
        }
        for(int i = 0;i < nums2.length;i++){
            nums[count++] = nums2[i];
        }
        Arrays.sort(nums);
        if(n % 2 != 0)
        return (double)(nums[n / 2]);
        else 
        return (nums[n/2]+nums[n/2-1]) / 2.0;

    }
}














































    //     int[] arr = new int[nums1.length + nums2.length];
    //     for(int i = 0;i < nums1.length;i++){
    //         arr[i] = nums1[i];
    //     }
    //     int k = 0;
    //      for(int i = nums1.length;i < nums1.length +nums2.length;i++){
    //         arr[i] = nums2[k++];
    //     }
    //     Arrays.sort(arr);
    //     if((nums1.length + nums2.length) / 2 != 0){
    //         return arr[(nums1.length + nums2.length) / 2];
    //     }
    //     else{
    //         int a = (nums1.length + nums2.length) / 2;
    //         double x = (arr[a] + arr[a - 1])/2;
    //         return x;
    //     }
    // }
