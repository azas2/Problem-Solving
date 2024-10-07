class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        my_check_list = []
        for can in range(len(candies)):
            result_with_candies = candies[can] + extraCandies  
            if result_with_candies >= max(candies):  
                my_check_list.append(True)  
            else:
                my_check_list.append(False)  
        return my_check_list
