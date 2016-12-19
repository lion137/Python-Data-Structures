# map (symbol table) implementation using binary search tree



class Binary_search_tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Tree_node(key, val)
        self.size += 1

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    # deletion part beginning
    def delete(self, key):
        if self.size > 1:
            node_removed = self._get(key, self.root)
            if node_removed:
                self._remove(node_removed)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def _remove(self, current):
        if current.isLeaf():  # is a leaf
            if current == current.parent.leftChild:
                current.parent.leftChild = None
            else:
                current.parent.rightChild = None
        elif current.hasBothChildren():  # is interior in a tree
            next_node = current.find_next()
            next_node._splice()
            current.key = next_node.key
            current.payload = next_node.payload

        else:  # has only one child (left or right)
            if current.hasLeftChild():
                if current.isLeftChild():
                    current.leftChild.parent = current.parent
                    current.parent.leftChild = current.leftChild
                elif current.isRightChild():
                    current.leftChild.parent = current.parent
                    current.parent.rightChild = current.leftChild
                else:
                    current.replaceNodeData(current.leftChild.key, current.leftChild.payload,
                                            current.leftChild.leftChild,
                                            current.leftChild.rightChild)
            else:
                if current.isLeftChild():
                    current.rightChild.parent = current.parent
                    current.parent.leftChild = current.rightChild
                elif current.isRightChild():
                    current.rightChild.parent = current.parent
                    current.parent.rightChild = current.rightChild
                else:
                    current.replaceNodeData(current.rightChild.key,
                                            current.rightChild.payload,
                                            current.rightChild.leftChild,
                                            current.rightChild.rightChild)

    def _find_next(self):
        res = None
        if self.hasRightChild():
            res = self.rightChild._find_min()
        else:
            if self.parent:
                if self.isLeftChild():
                    res = self.parent
                else:
                    self.parent.rightChild = None
                    res = self.parent._find_next()
                    self.parent.rightChild = self
        return res

    def _find_min(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def _splice(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    # end of deleting section

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.leftChild)
        else:
            return self._get(key, current.rightChild)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = Tree_node(key, val, parent=currentNode)

        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = Tree_node(key, val, parent=currentNode)
        else:
            currentNode.replaceNodeData(key, val, lc=currentNode.leftChild, rc=currentNode.rightChild)


class Tree_node:
    def __init__(self, key, val, left=None, right=None,
                 parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for item in self.leftChiLd:
                    yield item
            yield self.key
            if self.hasRightChild():
                for item in self.rightChild:
                    yield item



def inorder_traversal(tree):
    cur = tree.root
    def helper(current):
        if current:
            helper(current.leftChild)
            print(current.key, current.payload)
            helper(current.rightChild)
    return helper(cur)


def make_min_from_array(tree, xs):
    if len(xs) > 1:
        m = len(xs) // 2
        left = xs[:m]
        right = xs[m:]
        tree.put(xs[m], 0)
        make_min_from_array(tree, left)
        make_min_from_array(tree,right)

    else:
        tree.put(xs[0], 1)

def height(tree):
    if tree:
        l_height = height(tree.leftChild)
        r_height = height(tree.rightChild)
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1
    else:
        return 0

def height_node(tree_node):
    if not tree_node:
        return 0
    else:
        l_height = height_node(tree_node.leftChild)
        r_height = height_node(tree_node.rightChild)
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1

def is_balanced(tree_node):
    return abs(height_node(tree_node.root.leftChild) - height_node(tree_node.root.rightChild)) <= 1

def maxdepth(treenode):
    if treenode:
        return 1 + max(maxdepth(treenode.leftChild), maxdepth(treenode.rightChild))
    else:
        return 0


def mindepth(treenode):
    if treenode:
        return 1 + min(mindepth(treenode.leftChild), mindepth(treenode.rightChild))
    else:
        return 0


def is_balanced2(treenode):
    return maxdepth(treenode.root) - mindepth(treenode.root) <= 1

def top_height(tree_node):
    if not tree_node:
        return 0
    else:
        return 1 + top_height(tree_node.parent)

def make_list(tree_node):
    """ make a list from a bin tree"""
    if not tree_node:
        return []
    else:
        size = height_node(tree_node.root)
        l1 = [[] for x in range(size)]
        def travel_list(current):
                if current:
                    travel_list(current.leftChild)
                    l1[top_height(current) - 1].append(current.key)
                    travel_list(current.rightChild)
                return l1
        l = travel_list(tree_node.root)
        for x in range(len(l)):
            print(l[x])



