class TreeNode:
    def __init__(self,value) -> None:
        self.value = value
        self.children =  []

    def add_child(self,child_node):
        self.children.append(child_node)

    def remove_child(self,child_node):
        self.children.remove(child_node)    

class Tree:
    def __init__(self,root_value) -> None:
        self.root = TreeNode(root_value)

    def add_node(self,parent_value,value):
        parent_node = self.find_node(self.root,parent_value)

        if parent_node:
            parent_node.add_child(TreeNode(value))
        else:
            print("parent node not found")    


    def find_node(self,current_node,value):
        if current_node.value == value:
            return current_node
        
        for child in current_node.children:
            found_node = self.find_node(child,value)   
            if found_node:
                return found_node
            
        return None    
        
    def display(self,start_node=None):
        if start_node is None:
            start_node = self.root
        print(start_node.value,end='->')

        for child in start_node.children:
            self.display(start_node=child)

    def delete(self,node_to_delete):
        self.delete_node(self.root,node_to_delete)

    def delete_node(self,current_node,node_to_delete,parent=None):
        
        if current_node.value == node_to_delete:
            if parent:
                parent.remove_child(current_node)  
            else:
                self.root = None
            return    

        for child in current_node.children:
            self.delete_node(child,node_to_delete,parent=current_node)         
           
                


tree = Tree(1)
tree.add_node(1,2)
tree.add_node(1,3)
tree.add_node(1,4)
tree.add_node(3,6)
tree.add_node(4,5)
tree.delete(3)
tree.display()