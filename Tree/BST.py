class TreeNode:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
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
    
    def contains(self,key):
        return self.is_contains(self.root,key)

    def is_contains(self,node,key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.is_contains(node.left,key)
        else:
            return self.is_contains(node.right,key)
        
    def delete(self,key):
        self.root = self.delete_node(self.root,key)

    def delete_node(self,node,key):
        if node is None:
            return node
        
        if key > node.key:
            node.right = self.delete_node(node.right,key)

        elif key < node.key:
            node.left = self.delete_node(node.left,key) 

        else:
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            min_node = self.find_min(node.right)
            node.key = min_node.key
            node.right = self.delete_node(node.right,min_node.key)

        return node
        

    def find_min(self,node):

        while node.left is not None:
            node = node.left
        return node    

    def pre_order_traversal(self):
        self.pre_order_traversal_fun(self.root)

    def pre_order_traversal_fun(self,node):

        if node:
            print(node.key,end=' ')   
            self.pre_order_traversal_fun(node.left)  
            self.pre_order_traversal_fun(node.right)

    def post_order_travesal(self):
        self.post_order_travesal_fun(self.root)

    def post_oder_traversal_fun(self,node):
        if node:
            self.post_oder_traversal_fun(node.left)
            self.post_oder_traversal_fun(node.right)
            print(node.key,end=' ')

    def  in_order_traversal(self,node):
        self.in_order_traversal_fun(self.root)

    def in_order_traversal_fun(self,node):
        if node:
            self.in_order_traversal_fun(node.left)
            print(node.key,end=' ')    
            self.in_order_traversal_fun(node.right)

        
    def level_order_traversal(self):
        if not self.root:
            return

        queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            print(current_node.key, end=' ')

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)









bst = BinarySearchTree()
bst.insert(35)
bst.insert(30)
bst.insert(37)
bst.insert(28)
bst.insert(31)
bst.insert(38)
bst.insert(36)
bst.insert(34)

print(bst.contains(3))
bst.pre_order_traversal()
print()
bst.level_order_traversal()


            

        
    