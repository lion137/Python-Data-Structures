# Immutable stack interface based on Immutable lists (from this repo) 
class Stack:
    
    def __init__(self, elem = None, lst = None):
        if elem is not None:
            self.stack = Create_from_list(elem, lst)
        else:
            self.stack = Create_list([])
        
    def push(self, elem):
        return Stack(elem, self.stack)
        
        
    def pop(self):
        return remove_nth(0, self.stack) 
    
    def is_empty(self):
        return empty(self.stack)
    
    def peek(self):
        return nth(0, self.stack)
    
    def __str__(self):
        if self.stack is Nil:
            return '()'
        else:
            return self.stack.__str__()
        
s1 = Stack()
s2 = s1.push(1)
print(s2.is_empty())
print(s2)
