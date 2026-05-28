class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # Update best candidate
        def update(node, length, idx):
            if length < node.length:
                node.length = length
                node.idx = idx

        # Insert reversed container words
        for i, word in enumerate(wordsContainer):
            rev = word[::-1]
            node = root
            update(node, len(word), i)

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                update(node, len(word), i)

        ans = []

        # Query
        for word in wordsQuery:
            rev = word[::-1]
            node = root

            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.idx)

        return ans