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

        self.prefix_word_searcher(node,prefix,new)  
        return new

    def prefix_word_searcher(self,node,prefix,new):
        if node.end:
            new.append(prefix)   

        for char , child_node in node.child.items():
            self.prefix_word_searcher(child_node,prefix+char,new)
      

    def delete_word(self,word):
        def _delete(node,word,depth):
            if not node:
                return False
            
            if depth == len(word):
                if node.end:
                    node.end = False
                return len(node.child) == 0    
            
            char = word[depth]
            if char in node.child:
                should_delete_child = _delete(node.child[char],word,depth+1)

                if should_delete_child:
                    del node.child[char]

                    return len(node.child) == 0 and not node.end

            return False


        _delete(self.root,word,0)
        
    
trie = Trie()

name = ['messi','romero','depaul','ronaldo']   
for i in name:
    trie.insert(i)
trie.delete_word('romero')
print(trie.prefix_search('') )


          