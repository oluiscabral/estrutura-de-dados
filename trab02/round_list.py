class RoundList:
    def __init__(self):
        self.lst = list()
        self.i = 0

    def append(self, value):
        self.lst.append(value)

    def pop(self):
        if self.i == len(self.lst) - 1:
            ret = self.lst.pop(self.i)
            self.i = 0
            return ret
        return self.lst.pop(self.i)

    def reset(self):
        self.lst.clear()
        self.i = 0

    def __iter__(self):
        if self.lst:
            return self
        return iter([])

    def __next__(self):
        if self.lst:
            ret = self.lst[self.i]
            self.update_initial()
            return ret
        raise Exception("There is no value in the data structure.")

    def update_initial(self, n=1):
        """
        This method set the next `n` value as
        the first one to get next or get popped out.
        """
        self.i = (self.i + n) % len(self.lst)

    def __len__(self):
        return len(self.lst)
