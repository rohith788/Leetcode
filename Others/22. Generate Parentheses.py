class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        left = right = n
        ans = []
        def generate(s: str, l: int, r:int):
            if l < 1 and r < 1:
                ans.append(s)
                return
            if l > 0:
                generate(s+'(', l-1, r)
            if r > l:
                generate(s+')', l, r-1)
        generate('', left, right)
        return ans
        