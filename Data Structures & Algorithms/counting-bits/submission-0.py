class Solution:
    def countBits(self, n: int) -> List[int]:
        m=[]
        for i in range(n+1):
            m.append(i)
        res=[]
        for i in m:
            res.append(bin(i).count('1'))
        return res
