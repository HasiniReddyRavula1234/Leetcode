class Solution {
    public void rotate(int[] arr, int k) {
        if(arr.length == 0 || arr.length == 1 || k == 0)
         return;
        int n = arr.length;
        k = k % n;
        rotation(arr,0,n-1);
        rotation(arr,0,k-1);
        rotation(arr,k,n - 1);
    }
    public int[] rotation(int[] arr,int i,int j){
        while(i < j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j--;
        }
        return arr;
    }
}


    















































        //  if(k ==0 || nums.length <= 1)
        //  return;
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
        
//         return ;
//     }
// }
//  k = k % nums.length;
//         reverse(nums,0,nums.length - 1);
//         reverse(nums,0,k -1);
//         reverse(nums,k,nums.length - 1);
//     }
//         public  void reverse(int[] arr,int start,int end){
//             while(start < end){
//                 int temp = arr[start] ;
//                 arr[start] = arr[end];
//                 arr[end] = temp;
//                 start++;
//                 end--;
//             }
//         }
// }
  