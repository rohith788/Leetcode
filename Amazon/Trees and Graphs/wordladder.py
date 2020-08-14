class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord: return 0
        L = len(endWord)
        word_graph = defaultdict(list)
        for word in wordList:
            for i in range(L):
                temp_word = word[:i] + "*" + word[i+1:]
                word_graph[temp_word].append(word)
        q = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        # print(word_graph)
        while q:
            current_word, level = q.popleft()
            for i in range(L):
                temp_word = current_word[:i] + "*" + current_word[i+1:]
                for word in word_graph[temp_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        q.append((word, level+1))
                word_graph[temp_word] = []
        return 0
    