from typing import List, Tuple


class Node:
    def __init__(self) -> None:
        self.next: List['Node|None'] = [None] * 26
        self.occur: int = 0
        self.isWord = False

    def __str__(self) -> str:
        return f'{[chr(i + ord("a")) for i in range(26) if self.next[i] != None]}'


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        present: set[str] = set()
        for l in board:
            present.update(l)
        # Build Trie
        for word in words:
            curr: Node = root
            if not all([chr in present for chr in word]):
                continue
            for chr in word:
                if curr.next[ord(chr) - ord('a')] == None:
                    curr.next[ord(chr) - ord('a')] = Node()
                curr = curr.next[ord(chr) - ord('a')]  # type:ignore
                curr.occur += 1
            curr.isWord = True
        if root.next[0] and root.next[0].next[0]:
            print(root.next[0].occur)
            print(root.next[0].next[0].occur)

        words: set[str] = set()
        for x in range(len(board)):
            for y in range(len(board[0])):
                queue: List[Tuple[int, int, Node | None, List[Tuple[int, int]]]] = [
                    (x, y, root.next[ord(board[x][y]) - ord('a')], [])
                ]
                while len(queue) > 0:
                    i, j, curr, vis = queue.pop()  # type:ignore
                    if (i, j) in vis or curr == None or curr.occur == 0:
                        # if curr and curr.occur == 0:
                        #     print(''.join([board[i][j] for i, j in vis]), words)
                        continue
                    vis.append((i, j))
                    if curr.isWord:
                        words.add(''.join([board[i][j] for i, j in vis]))
                        tmp = root
                        for chr in [board[i][j] for i, j in vis]:
                            tmp = tmp.next[ord(chr) - ord('a')]
                            tmp.occur -= 1

                    for l, m in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if l < 0 or l >= len(board) or m < 0 or m >= len(board[0]):
                            continue
                        queue.append(
                            (
                                l,
                                m,
                                curr.next[ord(board[l][m]) - ord('a')],
                                [t for t in vis],
                            )
                        )
        return list(words)
