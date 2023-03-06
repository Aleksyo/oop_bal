import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


names = [Line, Rect, Ellipse]
elements = [random.choice(names)(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for _ in range(0, 217)]
for el in elements:
    if isinstance(el, Line):
        el.sp, el.ep = (0, 0), (0, 0)
