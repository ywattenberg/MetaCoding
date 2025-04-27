from typing import List, Optional


class Node:
    def __init__(self, isEnd: bool):
        self.children: List['Node| None'] = [None] * 26
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.root = Node(True)

    def insert(self, word: str) -> None:
        curr: Node = self.root
        # word = word.lower()
        for char in word:
            num = ord(char) - ord('a')
            if curr.children[num] != None:
                curr = curr.children[num]
            else:
                curr.children[num] = Node(False)
                curr = curr.children[num]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr: Node = self.root
        for char in word:
            num = ord(char) - ord('a')
            if curr.children[num] != None:
                curr = curr.children[num]
            else:
                return False
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr: Node = self.root
        for char in word:
            num = ord(char) - ord('a')
            if curr.children[num] != None:
                curr = curr.children[num]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)]
