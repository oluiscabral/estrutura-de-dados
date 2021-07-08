from round_list import RoundList


class JosephusSolver:
    def __init__(self):
        self.__n = 1
        self.__m = 1
        self.__lst = RoundList()

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        if n < 0:
            self.__n = 0
        else:
            self.__n = n

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, m):
        if m < 0:
            self.__m = 0
        else:
            self.__m = m

    def solve(self):
        if self.is_basic():
            return 1
        return self.heavy_solution()

    def is_basic(self):
        return self.is_power_of_2(self.n) and self.m == 1

    def is_power_of_2(self, n):
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True

    def heavy_solution(self):
        self.__init_values()
        ret = self.__last_standing()
        self.__lst.reset()
        return ret

    def __init_values(self):
        for i in range(self.n):
            self.__lst.append(i+1)

    def __last_standing(self):
        if len(self.__lst) == 0:
            return None
        while len(self.__lst) > 2:
            self.__pop_next()
        return next(self.__lst)

    def __pop_next(self):
        self.__update_initial()
        self.__lst.pop()

    def __update_initial(self):
        prev_i = self.__lst.i
        self.__lst.update_initial(self.m)
        if prev_i == self.__lst.i:
            self.__lst.update_initial()
