class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dict = {w:i for i, w in enumerate(S)}
        # dict.sort(key=lambda: x.values())
        ans = []
        index = 0
        prev = 0
        for i in range(len(S)):
            temp = dict[S[i]]
            if temp > index:
                index = temp
            if index == i:
                ans.append(temp-prev+1)
                prev = index+1
        return ans