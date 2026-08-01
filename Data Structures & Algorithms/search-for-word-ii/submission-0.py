class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:

    def findWords(self, board, words):

        root = TrieNode()

        # Build Trie
        for word in words:

            node = root

            for ch in word:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.word = word

        rows = len(board)
        cols = len(board[0])

        ans = []

        def dfs(r, c, node):

            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols
            ):
                return

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            node = node.children[ch]

            if node.word:
                ans.append(node.word)
                node.word = None      # avoid duplicates

            board[r][c] = "#"

            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)

        return ans