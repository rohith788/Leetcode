class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_arr = []
        for i in range(n):
            xor_arr.append(start + 2*i)
        xor = xor_arr[0]
        for i in range(1, n):
            xor ^= xor_arr[i]  
        return xors