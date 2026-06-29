class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e=[]
        for i in nums:
            
            if i in e:
                return True
                break
            else:
                e.append(i)
        return False