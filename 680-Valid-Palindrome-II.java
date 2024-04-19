class Solution {
  
public boolean validPalindrome(String s) {
   int left=0;
   int right=s.length()-1;
   char[]myArray=s.toCharArray();

   while (left<right){
       if(myArray[left]==myArray[right]){
           left++;
           right--;
       }
       else {
           return isPalindrome(myArray,left+1,right)||
                   isPalindrome(myArray,left,right-1);
       }
   }
   return true;
}
public boolean isPalindrome(char[]s, int left,int right){
    while (left<right){
        if(s[left]==s[right]){
            left++;
            right--;
        }
        else
            return false;
    }
    return true;
}

}