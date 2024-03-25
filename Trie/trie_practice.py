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
    
    def prefix_search(self,prefix):
        node = self.root
        new = []

        for char in prefix:
            if char not in node.child:
                return []
            node = node.child[char]

        self.prefix_searcher(node,prefix,new)

        return new


    def prefix_searcher(self,node,prefix,new):
        if node.end:
            new.append(prefix)

        for char ,child_node in node.child.items():
            self.prefix_searcher(child_node,prefix+char,new)  


   
trie = Trie()

name = ['messi','romero','depaul','ronaldo']   
for i in name:
    trie.insert(i)

print(trie.prefix_search('') )


