# Recursive definition of  binary search tree (immutable)
# I follows a grammar:
# Binary-search-tree :: = () | (Val Binary-search-tree Binary-search-tree) Val should support >, <, =
# is empty or it's a list of Int and two binary trees
# there's gonna be right and left subtree
# The interface strictly follow this definition

class Nil_tree:
    """class Nil_tree, the empty tree"""
    
    def is_empty(self):
        return True
    def left(self):
        return Exception("Empty")
    def right(self):
        return Exception("Empty")
    def __str__(self):
        return "()"
    
class Binary_tree:
    """Class Binary_tree, the non empty tree: ( val, left, right)"""
            
    def __init__(self, _item, _left, _right):
        self.item = _item
        self.left = _left
        self.right = _right
        
    def is_empty(self):
        return False


        
class Tree(metaclass=ABCMeta):
    
    @abstractmethod
    def is_empty():
        pass
    def item():
        pass
    def left():
        pass
    def right():
        pass
    
List.register(Nil_tree);
List.register(Binary_tree)

# few tree methods:
def inorder(tree):
    """Inorder traversal"""
    if tree is Nil_tree:
        return Nil_tree
    else:
        inorder(tree.left)
        print(tree.item)
        inorder(tree.right)

def make_tree(item, left_branch, right_branch):
    """Makes a tree, item is  any python value 
    left and right branches are trees, possible empty"""
    return Binary_tree(item, left_branch, right_branch)

def is_element(elem, tree):
    """Check if elem is in binary tree"""
    if tree is Nil_tree:
        return False
    elif elem < tree.item:
        return is_element(elem, tree.left)
    elif elem > tree.item:
        return is_element(elem, tree.right)
    else:
        return True
    
def join_tree(elem, tree):
    """Add eleme to the binary tree returns tree if
    elem is already there"""
    if tree is Nil_tree:
        return make_tree(elem, Nil_tree, Nil_tree)
    elif elem < tree.item:
        return make_tree(tree.item, join_tree(elem, tree.left), tree.right)
    elif elem > tree.item:
        return make_tree(tree.item, tree.left, join_tree(elem, tree.right))
    else:
        return tree
