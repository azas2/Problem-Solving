class Solution {
 fun runningSum(nums: IntArray): IntArray {
   var myarr: IntArray = IntArray(nums.size)
   var countrunnig = 0
   for (i in 0 until  nums.size) {
      countrunnig += nums[i]
      myarr[i] = countrunnig
   }

   return myarr
}
}