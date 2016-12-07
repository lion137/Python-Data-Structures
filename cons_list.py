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


def nth(n, xs):
    """Returns nt-h (0 based indexing) elemt of the list,
    throws an exception when out of range"""
    if xs is Nil:
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


def cons(elem, xs):
    """Cons element elem to the list"""
    return Cons(elem, xs)


def subs_in_expr(new, old, xs):  # this helper function works put single list element which maybe list itself
    if xs is not Cons:
        if xs == old:
            return new
        else:
            return xs
    else:
        return subst(new, old, xs)


def subst(new, old, xs):  # substitutes new as old in a list(possible nested)
    if xs is Nil:
        return Nil
    else:
        return cons(subs_in_expr(new, old, xs.head), subst(new, old, xs.tail))


def Create_list(args):
    """Crates immutable list from any iterable args"""
    if len(args) == 0:
        return Nil()
    tmp = len(args) - 1

    def helper(xs, cnt, limit):
        if cnt > limit:
            return Nil
        else:
            return cons(xs[cnt], helper(xs, cnt + 1, limit))

    return helper(args, 0, tmp)


def duplicate(n, xs):
    """return n duplicates n times expression xs"""
    if n == 0:
        return Nil
    else:
        return xs | c | duplicate(n - 1, xs)


def to_list(*args):
    """Create a single element cons list from an argument/s"""
    if args is None:
        return Nil()
    else:
        return Cons(args, Nil)
