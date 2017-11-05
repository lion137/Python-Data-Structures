from _collections_abc import ABCMeta, abstractmethod
# immutable cons list and methods:
class Nil:
    """class Nil, the empty list"""

    def is_empty(self):
        return True

    def head(self):
        return Exception("Empty")

    def tail(self):
        return Exception("Empty")

    def get_next(self):
        return None

    def __str__(self):
        return "()"


class Cons:
    """Class cons, the non empty list: (head, list)"""

    def __init__(self, _head, _tail):
        self.head = _head
        self.tail = _tail

    def is_empty(self):
        return False

    def get_next(self):
        return self.tail

    def __str__(self):
        current = self.tail
        out = "(" + str(self.head)
        while current != Nil:
            out += ' ' + str(current.head)
            current = current.get_next()
        return out + ')'


class List(metaclass=ABCMeta):
    @abstractmethod
    def is_empty():
        pass

    def head():
        pass

    def tail():
        pass


List.register(Nil);
List.register(Cons)

def concat(xs, ys): 
    """Concatenates two lists"""
    if xs is Nil:
        return ys
    else:
        return cons(xs.head, concat(xs.tail, ys)) 
    
    
def nth(n , xs):
    """Returns nt-h (0 based indexing) elemt of the list, 
    throws an exception when out of range"""
    if empty(xs):
        return Exception("Out Of Bound")
    if n == 0:
        return xs.head
    else:
        return nth(n - 1, xs.tail)

def length(xs):
    """Returns length of a list O(n)"""
    if xs is Nil:
        return 0
    else:
        return 1 + length(xs.tail)
def empty(xs):
    if xs is Nil:
        return True
    else:
        return False

def cons(elem ,xs):
    """Cons element elem to the list"""
    return Cons(elem, xs)


#------ helper function:---------------
def subs_in_expr(new, old, xs): # this helper function works put single list element which maybe list itself
    if xs is not Cons:
        if xs == old:
            return new
        else:
            return xs
    else:
        return subst(new, old, xs)
    
def subst(new, old, xs):
    """substitutes new as old in a list(possible nested)"""
    if xs is Nil:
        return Nil
    else:
        return cons(subs_in_expr(new, old, xs.head) , subst(new ,old, xs.tail))

def Create_list(args):
    """Crates immutable list from any iterable args"""
    if args is None:
        return Nil()
    tmp = len(args) - 1
    def helper(xs, cnt, limit):
        if cnt > limit:
            return Nil
        else:
            return Cons(xs[cnt], helper(xs, cnt + 1, limit))
    return helper(args, 0, tmp)

def Create_from_list(elem = None, lst = None):
    if elem is not None:
        return Cons(elem, lst)
    else:
        return Nil()


def duplicate(n, xs):
    """return n duplicates n times expression xs"""
    if n == 0:
        return Nil
    else:
        return cons(xs, duplicate(n - 1, xs))

def to_list(*args):
    """Create a single element cons list from an argument/s"""
    if args is None:
        return Nil()
    else:
        return Cons(args, Nil)


def my_map(f, xs): # my_map to not cover map from std
    """Standart map, map a function onto a list"""
    if xs is Nil:
        return Nil
    else:
        return f(xs.head) |c| my_map(f, xs.tail)

def my_filter(pred, xs): # to not cover filter from std
        """Filter on list"""
        if xs is Nil:
            #pdb.set_trace()
            return Nil
        else:
            if pred(xs.head):
                return cons(xs.head, my_filter(pred, xs.tail))
            else:
                return my_filter(pred, xs.tail)
            
def remove_nth(n, xs):
    """Removes the n-th elem from the list, throw an Exception
    if index out of bounds"""
    if isinstance(xs, Nil):
        return Exception("Out of Bounds")
    else:
        if n == 0:
            if xs.tail is not Nil:
                return cons(xs.tail.head, xs.tail.tail)
            else:
                return Nil
        else:
            return cons([xs.head, remove_nth(n - 1, xs.tail)])
        
def down(xs):
    """Wrap parenthesis every each top level expression"""
    return my_map(lambda x: Cons(x, Nil), xs)



def list_set(xs, n, elem):
    """Returns list with n - th element updated to elem"""
    if isinstance(xs, Nil):
        return Exception("Out of Bounds")
    else:
        if n == 0:
            return cons(elem, xs.tail)
        else:
            return cons(xs.head, list_set(xs.tail, n - 1, elem))
        

#-------helper function:-----------------------
def count_occurencies_nested(x, xs):
    """ cont_ocurencies helper, returns number of occurencies in an expression"""
    if not isinstance(xs, Cons):
        if xs == x:
            return 1
        else:
            return 0
    else:
        return count_occurencies(x, xs)
    
def count_occurencies(x, xs):
    """Count occurencies of x in xs (possible nested)"""
    if xs is Nil:
        return 0
    else:
        return count_occurencies_nested(x, xs.head) + count_occurencies(x, xs.tail)
    
#----------helper function:-------------
def product_helper(x, ys):
    """Building a list of pairs - multiplies elem x times list ys """
    if ys is Nil:
        return Nil
    else:
        return cons(Cons(x, ys.head), product_helper(x, ys.tail))

    
def product(xs, ys):
    """Returns cartesian product of two lists (lists are without
    repetitions)."""
    if xs is Nil:
        return Nil
    else:
        return cons(product_helper(xs.head, ys), product(xs.tail, ys))

def reverse(xs, ys):
    """reverse a list"""
    if empty(ys):
        return xs
    else:
        return reverse(cons(ys.head, xs), ys.tail)

def reduce(f, ys, start):
        """Reduce left, start is the neutral element of f"""
        def helper(f, xs, acc):
            if xs is Nil:
                return acc
            else:
                return helper(f, xs.tail, f(acc, xs.head))
        return helper(f, ys, start)

def insert(elem, n, xs):
    """Inserts elem in a position after index n"""
    if xs is Nil:
        return Exception("Out of bounds")
    else:
        if n == 0:
            return cons(xs.head, Cons(elem, xs.tail))
        else:
            return cons(xs.head, insert(elem, n - 1, xs.tail))
