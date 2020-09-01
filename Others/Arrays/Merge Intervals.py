class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        if len(intervals) == 1: return intervals
        intervals.sort(key=lambda x: x[0])
        ans = []
        for i in intervals:
            
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(i[1], ans[-1][1])
            print(ans)
        return ans
    
    
    
    
    
    
    
    
    
