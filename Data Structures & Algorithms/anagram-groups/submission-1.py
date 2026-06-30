class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        e={}
        for w in strs:
            freq=[0]*26
            for c in w:
                freq[ord(c)-ord("a")]+=1
            key=tuple(freq)
          
            if key not in e:
                e[key]=[]
            e[key].append(w)
        return list(e.values())