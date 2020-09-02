class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # dict = {}
        dict = Counter(words)
        # for x in words:
        #     if x in dict:
        #         dict[x] += 1
        #     else:
        #         dict[x] = 1
        # print(count_dict, dict)
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]
    
        # ans = sorted(count_dict, key=lambda w: (-count_dict[w], w))
        # ans = [k for k in count_dict]
        # return ans[:k]