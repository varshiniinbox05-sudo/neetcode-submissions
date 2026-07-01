class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        
        return res



    def decode(self, s: str) -> List[str]:
        a = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1

            l = int(s[i:j])

            res = ""
            for k in range(j + 1, j + 1 + l):
                res += s[k]

            a.append(res)

            i = j + 1 + l     

        return a
        
        
