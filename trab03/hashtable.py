class HashTable:
    def __init__(self, size):
        self.__lst = self.__create_list(size)

    def __create_list(self, size):
        lst = []
        for i in range(size):
            lst.append(-1)
        return lst

    def insert(self, text):
        i = len(text) % len(self.__lst)
        if not self.is_empty(i):
            i = self.find_empty(i)
        self.__lst[i] = text

    def is_empty(self, i):
        return self.__lst[i] == -1 or self.__lst[i] == -2

    def find_empty(self, ref=0):
        for n in range(1, len(self.__lst)):
            i = self.__get_round_index(ref, n)
            if self.is_empty(i):
                return i
        raise Exception('Error: could not find an empty cell, table is full.')

    def __get_round_index(self, ref, n):
        return (ref + n) % len(self.__lst)

    def remove(self, text):
        i = self.__lst.index(text)
        self.__lst[i] = -2

    def __str__(self):
        s = ''
        for v in self.__lst:
            s += str(v) + '\n'
        return s[:-1]

