class TreeNode:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None

class Tree:
    
    def __init__(self) -> None:
        self.root = None

    def insert(self,key):
        self.root = self.insert_node(self.root,key)

    def insert_node(self,node,key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self.insert_node(node.left,key)
        elif key > node.key:
            node.right = self.insert_node(node.right,key)

        return node

    def delete(self,key):
        self.root = self.delete_node(self.root,key)

    def delete_node(self,node,key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_node(node.left,key)
        elif key > node.key:
            node.right = self.delete_node(node.right,key) 
        else:
            if node.right is None:
                return node.left
            elif  node.left is None:
                return node.right
            
            min_node = self.find_min(node.right)
            node.key = min_node.key
            node.right = self.delete_node(node.right,min_node.key)

    def find_min(self,node):

        while node.left is not None:
            node = node.left
        return node     
        
    def contains(self,key):
        return self.is_contains(self.root,key)

    def is_contains(self,node,key):

        if node is None:
            return False
        
        if node.key == key:
            return True
        
        elif key < node.key:
            return self.is_contains(node.left,key)
        else:
            return self.is_contains(node.right,key)    
            
             
    def pre_order_traversal(self):
        self.pre_order_traversal_fun(self.root)

    def pre_order_traversal_fun(self,node):

        if node:
            print(node.key,end=' ')
            self.pre_order_traversal_fun(node.left)
            self.pre_order_traversal_fun(node.right)


    def closest(self,value):
        self.closest_key = self.root.key
        self.diff = abs(self.root.key-value)
        return self.closest_value(self.root,value)
    

    def closest_value(self,node,value):
        if node is None:
            return self.closest_key
        
        if abs(node.key - value) < self.diff:
            self.diff = abs(node.key-value)
            self.closest_key = node.key
        
        if value < node.key:
            return self.closest_value(node.left,value)
        else:
            return self.closest_value(node.right,value)   


        
        

    
        





bst = Tree()
bst.insert(35)
bst.insert(30)
bst.insert(37)
bst.insert(28)
bst.insert(31)
bst.insert(38)
bst.insert(36)
bst.insert(34)

print(bst.closest(39))

print(bst.contains(3))
bst.pre_order_traversal()
