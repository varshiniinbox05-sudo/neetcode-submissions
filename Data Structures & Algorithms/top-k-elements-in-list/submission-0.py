class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        arr=sorted(freq.items(), key=lambda x:x[1],reverse=True)
        r=[]
        for i in range(k):
            r.append(arr[i][0])
        return r

