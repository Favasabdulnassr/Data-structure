class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root

        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.end = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.end  
 
        
    
trie = Trie()

name = ['messi','romero','depaul','ronaldo']   
for i in name:
    trie.insert(name)

trie.print_trie()   


          