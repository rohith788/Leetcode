class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_wrd = set(banned)
        max_wrd = ""
        max_count = -1
        for c in "!?',;.":
          paragraph = paragraph.replace(c, " ")
        count = collections.Counter( word for word in paragraph.lower().split())
        for elem in count:
          if( count[elem] > max_count and elem not in banned_wrd):
            max_count = count[elem]
            max_wrd = elem
        return max_wrd