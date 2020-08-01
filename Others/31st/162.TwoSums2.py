class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1
        while( s < e ):
            tot = numbers[s] + numbers[e]
            if(tot == target): return ([s + 1, e + 1])
            elif(tot < target): s += 1
            else: e -= 1
        return None