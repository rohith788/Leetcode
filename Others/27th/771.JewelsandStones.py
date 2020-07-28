class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        for i in S:
            if(i in jewels.keys()): jewels[i] += 1
            else: jewels[i] = 1
                
        count = 0
        for j in J:
            if j in jewels.keys(): count += jewels[j]
                
        return count