import math


class Point:
    def __init__(self, id, pox, poy):
        self.id = id
        self.pox = pox
        self.poy = poy

    def in_eps(self, target, eps):
        dis = (self.pox - target.pox) ** 2 + (self.poy - target.poy) ** 2
        dis = math.sqrt(dis)
        return dis < eps

    def core_test(self, eps, minpt, inputs):
        in_my_eps = []
        num = 0
        for i in inputs:
            if i == self:
                continue
            if self.in_eps(i, eps):
                num = num + 1
                in_my_eps.append(i)
        if num >= minpt:
            return [True, in_my_eps]
        else:
            return [False, in_my_eps]
