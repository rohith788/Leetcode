class Solution:
    def Area(self, i1, i2, w1, w2):
            l = i2 - i1
            w = min(w2,w1)
            return (l * w)
    def maxArea(self, height: List[int]) -> int:
        A = 0
        i, j = 0, len(height) - 1
        while( i < j):
            A = max(A, self.Area(i, j, height[i], height[j]))
            if(height[i] < height[j]): i += 1
            else: j-= 1
        return A
            
            