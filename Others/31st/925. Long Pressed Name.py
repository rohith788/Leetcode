class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        la, lt = len(name), len(typed)
        i = j = 0
        while i < la and j < lt:
            if name[i] == typed[j]: i, j = i + 1, j + 1
            elif i > 0 and typed[j] == name[i-1]: j += 1
            else: return False
        return i == la and all(typed[i] == name[-1] for i in range(j, lt))