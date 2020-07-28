class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_map = {}
        for i in range(len(keyboard)):
            key_map[keyboard[i]] = i
        prev = 0
        count = 0
        for i in range(len(word)):
            count += abs(prev - key_map[word[i]])
            prev = key_map[word[i]]
        return count