class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Helper function for the standard linear House Robber problem
        def rob_linear(house_subset: list[int]) -> int:
            prev1 = 0  # max money that can be robbed up to previous house
            prev2 = 0  # max money that can be robbed up to two houses ago
            
            for current in house_subset:
                temp = max(prev1, prev2 + current)
                prev2 = prev1
                prev1 = temp
                
            return prev1

        # Compare robbing from house 0 to n-2 vs house 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))