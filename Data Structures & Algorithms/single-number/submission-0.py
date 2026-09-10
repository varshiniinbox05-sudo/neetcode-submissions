from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq=Counter(nums)
        for i,j in freq.items():
            if j==1:
                
                return i
        