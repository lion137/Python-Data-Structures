
class NaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.kids = None

    def insert(self, newNode):
        if self.kids:
            t = NaryTree(newNode)
            self.kids.append(t)
            t.parent = self
        else:
            t = NaryTree(newNode)
            self.kids = []
            self.kids.append(t)
            t.parent = self

    def setRootVal(self, obj):
        self.key.append(obj)

    def getRootVal(self):
        return self.key

    def getParent(self):
        return self.parent

    def getNthKid(self, i=-1): # return a child index i, the last one if i not specified
        return self.kids[i]

def traverse(tree): # tree traversal, DFS
    if tree:
        stk = []
        stk.append(tree)
        while len(stk) > 0:
            top = stk.pop()
            if top.kids:
                for child in top.kids:
                    stk.append(child)
            print(top.getRootVal())

    else:
        return None