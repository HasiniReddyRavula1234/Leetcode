class Solution {
    public void rotate(int[] nums, int k) {
//  if(k ==0 || nums.length <= 1)
//          return;
//         int n = nums.length- 1;
//         k = k % n;
//         reverse(nums,0,n);
//        reverse(nums,0,k-1);
//        reverse(nums,k,n);
        
//     }
//     public int[] reverse(int[] nums,int i, int j){
       
       
//             while(i < j){
//                 int temp = nums[i];
//                 nums[i] = nums[j];
//                 nums[j] = temp;
//                 i++;
//                 j--;
//             }
        
//         return nums;
//     }
// }
 k = k % nums.length;
        reverse(nums,0,nums.length - 1);
        reverse(nums,0,k -1);
        reverse(nums,k,nums.length - 1);
    }
        public  void reverse(int[] arr,int start,int end){
            while(start < end){
                int temp = arr[start] ;
                arr[start] = arr[end];
                arr[end] = temp;
                start++;
                end--;
            }
        }
}
  