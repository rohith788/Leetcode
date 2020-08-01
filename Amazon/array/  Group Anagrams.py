class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            if temp in d:
                d[temp].append(strs[i])
            else:
                d[temp] = [strs[i]]
        return d.values()
        
        
                