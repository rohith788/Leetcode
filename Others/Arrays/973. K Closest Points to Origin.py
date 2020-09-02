class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == 0 or len(points) < 1: return []
        dict = {}
        ans = []
        for i, point in enumerate(points):
            x, y = point
            dict[i] = math.sqrt(x**2 + y**2)
        sorted_dict = {k:v for k,v in sorted(dict.items(), key=lambda x:x[1])}
        arr = sorted_dict.keys()
        count = 1
        for i in arr:
            ans.append(points[i])
            if count == K: break
            count += 1
            
        return ans