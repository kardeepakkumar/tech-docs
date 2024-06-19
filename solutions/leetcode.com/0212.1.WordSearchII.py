class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.counts = 0

    def addWord(self, word):
        cur = self
        cur.counts += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.counts += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.counts -= 1
        for c in word:
            cur = cur.children[c]
            cur.counts -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)
        result = set()
        def dfs(r, c, word, node):
            if (
                r not in range(m) or
                c not in range(n) or
                board[r][c] not in node.children or
                node.children[board[r][c]] == 0
                ):
                return
            node = node.children[board[r][c]]
            word += board[r][c]
            ch = board[r][c]
            board[r][c] = '#'
            if node.isWord:
                node.isWord = False
                result.add(word)
                root.removeWord(word)
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)
            board[r][c] = ch
        for r in range(m):
            for c in range(n):
                dfs(r,c,"",root)
        return(list(result))
    

# metadata
# relevant-topics dfs, trie, prefix tree, backtracking
# time-complexity O(MN*4^MN) 5.00%
# space-complexity O(MN) 12.93%
# language python
# difficulty hard
# date 20240601