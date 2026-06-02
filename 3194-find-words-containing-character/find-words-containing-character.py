class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        s = []
        for i, word in enumerate(words):
            if x in word:
                s.append(i)
        return s