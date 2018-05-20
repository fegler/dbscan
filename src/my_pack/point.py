import math


class Point:
    def __init__(self, id, pox, poy):
        self.id = id
        self.pox = pox
        self.poy = poy
        self.status = None

    def in_eps(self, target, eps):
        dis = (self.pox - target.pox) ** 2 + (self.poy - target.poy) ** 2
        dis = math.sqrt(dis)
        return dis < eps

    def core_test(self, eps, minPt, inputs):
        eps_ele = []
        for i in inputs:
            if self.in_eps(i, eps):
                eps_ele.append(i)
        if len(eps_ele) >= minPt:
            return True, eps_ele
        else:
            return False, []
