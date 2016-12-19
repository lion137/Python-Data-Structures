# binary heap - min heap

class Bin_heap:
    def __init__(self):
        self.heap_list = [0]
        self.__current_size = 0

    def build_heap(self, xs):
        i = len(xs) // 2
        self.__current_size = len(xs)
        self.heap_list = [0] + xs[:]
        while i > 0:
            self.__pop_down(i)
            i = i - 1

    def del_min(self):
        res = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.__current_size]
        self.__current_size -= 1
        self.heap_list.pop()
        self.__pop_down(1)
        return res

    def insert(self, x):
        self.heap_list.append(x)
        self.__current_size += 1
        self.__pos_item(self.__current_size)

    def find_min(self):
        return self.heap_list[1]

    def size(self):
        return self.__current_size

    def __str__(self):
        return str(print(self.heap_list[1:]))

    def __len__(self):
        return self.size()

    # private methods

    def __pos_item(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2

    def __pop_down(self, i):
        while i * 2 <= self.__current_size:
            min_ch = self.__min_child(i)
            if self.heap_list[i] > self.heap_list[min_ch]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_ch]
                self.heap_list[min_ch] = tmp
            i = min_ch

    def __min_child(self, i):
        if i * 2 + 1 > self.__current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


h1 = Bin_heap()
h1.build_heap([8, 23, 5, 6, 77, 1, -98])
print(h1)
print(h1.find_min())
print(h1)
h1.del_min()
print(h1)
h1.insert(-909)
print(h1)
print(len(h1))
'''
output ->
[-98, 6, 1, 23, 77, 8, 5]
None
-98
[-98, 6, 1, 23, 77, 8, 5]
None
[1, 6, 5, 23, 77, 8]
None
[-909, 6, 1, 23, 77, 8, 5]
None
7
'''
