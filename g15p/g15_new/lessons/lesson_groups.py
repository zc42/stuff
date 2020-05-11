class Lsn:
    def __init__(self, g=int, lesson_nb=None, h_xy=()):
        self.g = g
        self.lesson_nb = lesson_nb
        self.h_xy = h_xy
        self.done = False

    def __str__(self) -> str:
        if self.lesson_nb == None: return str(self.g)
        # ---------
        s = str(self.g) + ", " + \
            str(self.lesson_nb) + ", " + \
            str(self.h_xy)
        return s

    def get_tuple(self):
        return (self.g, self.lesson_nb, self.h_xy)


class Lesson_group:
    def __init__(self, a=[Lsn], name=str):
        self.a = a
        self.name = name
        self.done = False

    def __str__(self) -> str:
        s = ""
        for a in self.a:
            s += 'Lsn(' + str(a) + '), '
        if len(s) > 0: s = s[:-2]
        return self.name + ' = [' + s + ']'

    # def get_tuple_list(self):
    #     return list(map(lambda x: x.get_tuple(), self.a))


class Lesson_groups:
    def __init__(self, a=[Lesson_group]):
        self.a = a

    def __str__(self) -> str:
        s = ""
        for a in self.a:
            s += str(a) + '\n'
        return s

def get_lessons_one_case(l=Lsn):
    lg1 = Lesson_group([l], "lessons_one_case.txt")
    return Lesson_groups([lg1])