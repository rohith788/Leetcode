class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        c = 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                c = c*10 + int(s[i])
            elif s[i].isalpha():
                ans += s[i]
            elif s[i] == '[':
                print(ans, c)
                stack.append((ans, c))
                ans = ""
                c = 0
            elif s[i] == ']':
                txt, num = stack.pop()
                ans = txt + ans * num
        return ans
