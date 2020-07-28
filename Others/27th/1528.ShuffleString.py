class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = [''] * len(s)
        for i, c in enumerate(s):
            temp[indices[i]] = c
        return "".join(temp)