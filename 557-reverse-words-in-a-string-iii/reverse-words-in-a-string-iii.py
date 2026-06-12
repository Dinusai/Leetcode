class Solution:
    def reverseWords(self, s: str) -> str:
        s1=s.split()
        rev=[i[::-1] for i in s1]
        return ' '.join(rev)
