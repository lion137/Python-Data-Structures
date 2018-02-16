# binary tree
import Stack as st
def preorder_traversal(tree):
    if tree:
        print(tree.getRootVal())
        preorder_traversal(tree.getLeftChild())
        preorder_traversal(tree.getRightChild())


def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.getLeftChild())
        postorder_traversal(tree.getRightChild())
        print(tree.getRootVal())


def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.getLeftChild())
        print(tree.getRootVal())
        inorder_traversal(tree.getRightChild())

def inorder_traversal_check(tree, diff = 0):
    "Check if binary tree is balanced"
    if tree:
        inorder_traversal_check(tree.getLeftChild())
        if abs(height(tree.getLeftChild()) - height(tree.getRightChild())) > 1:
            diff = 1
        inorder_traversal_check(tree.getRightChild())
        if diff == 1:
            return False
        else:
            return True
    else:
        return True

def size(tree):
    if tree:
        return size(tree.getLeftChild()) + 1 + size(tree.getRightChild())
    else:
        return 0

def height(tree):
    if tree:
        l_height = height(tree.getLeftChild())
        r_height = height(tree.getRightChild())
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1
    else:
        return 0


class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            t = BinaryTree(newNode)
            self.leftChild = t
            t.parent = self
            # self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.parent = self
            t.leftChild = self.leftChild
            self.leftChild.parent = t
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            t = BinaryTree(newNode)
            self.rightChild = t
            t.parent = self
            # self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.parent = self
            t.rightChild = self.rightChild
            self.rightChild.parent = t
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getParent(self):
        return self.parent

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


def inorder_iter(tree):
    current = tree
    s = st.Stack()
    is_done = False
    while not is_done:
        if current:
            s.push(current)
            current = current.leftChild
        else:
            if not s.is_empty():
                current = s.pop()
                print(current.key)
                current = current.rightChild
            else:
                is_done = True

tr1 = BinaryTree("a")
print("root->",tr1.getRootVal())
tr1.insertLeft("b")
print("root->left ", tr1.getLeftChild().getRootVal())
tr1.getLeftChild().insertRight("d")
print("rot->left->right ", tr1.getLeftChild().getRightChild().getRootVal())
tr1.insertRight("c")
tr1.getRightChild().insertLeft("e")
tr1.getRightChild().insertRight("f")
tr1.getRightChild().getRightChild().insertRight("g")
#tr1.getRightChild().getRightChild().getRightChild().insertRight("h")
inorder_iter(tr1)
(inorder_traversal_check(tr1.getRightChild()))
'''
root-> a
root->left  b
rot->left->right  d
b
d
a
e
c
f
g
'''
