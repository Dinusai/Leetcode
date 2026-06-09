class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len((ch).split()) for ch in sentences )
    
        