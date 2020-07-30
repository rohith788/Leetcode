class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        tot, l_p = 0, points[0]
        for p in points:
            tot += max(abs(p[0] - l_p[0]), abs(p[1] - l_p[1]))
            l_p = p
        return(tot)