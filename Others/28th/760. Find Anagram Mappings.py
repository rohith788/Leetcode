class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        map_anagram = {}
        arr = []
        for j in range(len(B)):
            map_anagram[B[j]] = j
        for i in A:
            if(i in map_anagram):
                arr.append(map_anagram[i])
        return arr