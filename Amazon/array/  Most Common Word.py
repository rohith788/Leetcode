class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower()
		
        for c in "!?.;',":
           p = p.replace(c, ' ') 
		   
        d = Counter(p.split())
        for word in banned:
            if word.lower() in d:
                del d[word]
        v,k = max((v,k) for k,v in d.items())
        return k