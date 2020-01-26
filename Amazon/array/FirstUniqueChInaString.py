class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_map = {} 
        word_count = {}
        count = 0
        for i in s:
          print()
          if(i in word_map):
            word_map[i] += 1
          else:
            word_count.update({i : count})
            word_map.update({i : 0})
          count += 1
        for k in word_map.keys():
          if word_map[k] == 0:
            return word_count[k]
        return -1