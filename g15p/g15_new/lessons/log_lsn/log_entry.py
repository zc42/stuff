import datetime
import functools
import pathlib

# from past.builtins import cmp
# from __builtin__ import cmp

from g15_new.lessons.lessons_v2 import Lessons_v2

min_pass_nb = 5


class Log_entry:
    def __init__(self, l=Lessons_v2, fail=bool):
        self.init(l.g, l.lesson_nb, l.l_indx, l.current_lesson[2], fail)

    def init(self, g=int, l_nb=int, l_indx=int, xy_h=(), fail=bool):
        self.g = g
        self.l_indx = l_indx
        self.l_nb = l_nb
        self.xy_h = xy_h

        self.run_nb = 1
        self.pass_first = 1 if not fail else 0
        self.pass_last = 1 if not fail else 0
        self.fail_last = 1 if fail else 0
        a = self.pass_last - self.fail_last
        self.done = a >= min_pass_nb

    def update(self, fail=bool):
        self.run_nb = self.run_nb + 1
        self.pass_first = self.run_nb if not fail and self.pass_last == 0 else self.pass_first
        self.pass_last = self.run_nb if not fail else self.pass_last
        self.fail_last = self.run_nb if fail else self.fail_last
        a = self.pass_last - self.fail_last
        self.done = a >= min_pass_nb
        return self

    def str(self):
        return '(' + str(self.g) \
               + ', ' + str(self.l_nb) \
               + ', ' + str(self.xy_h) + ')' \
               + '\t| l indx: ' + str(self.l_indx) \
               + '\t| r nb: ' + str(self.run_nb) \
               + '\t| fail l: ' + str(self.fail_last) \
               + '\t| pass f: ' + str(self.pass_first) \
               + '\t| pass l: ' + str(self.pass_last) \
               + '\t| done: ' + str(self.done)


def cmp(x, y):
    """
    cmp(x, y) -> integer

    Return negative if x<y, zero if x==y, positive if x>y.
    """
    if x < y: return -1
    if x > y: return 1
    return 0


class Log:
    def __init__(self, log_dir=str, test_name=str):
        self.log_dir = log_dir
        self.t1 = datetime.datetime.now()
        self.test_name = test_name
        self.log = dict()

    def add(self, l=Lessons_v2, fail=bool):
        self.log_name = l.get_log_name()
        o = self.get_entry(l)
        o = self.update_entry(o, l, fail)
        self.log[l.l_indx] = o

    def update_entry(self, o, l=Lessons_v2, fail=bool):
        return Log_entry(l, fail) \
            if o is None \
            else o.update(fail)

    def get_entry(self, l=Lessons_v2):
        return self.log[l.l_indx] \
            if l.l_indx in self.log \
            else None

    def write(self):
        s = ''

        l = list(self.log.values())
        l = sorted(l, key=functools.cmp_to_key(self.cmp_entry))

        for v in l:
            s = s + v.str() + '\n'

        pathlib.Path(self.log_dir).mkdir(parents=True, exist_ok=True)
        fn = self.log_dir + self.log_name
        file1 = open(fn, 'w')
        self.write_time(file1)
        file1.writelines(s)
        file1.close()

    def write_time(self, file1):
        t1_str = self.t1.strftime('%Y.%m.%d %H:%M:%S')
        t2 = datetime.datetime.now()
        d = '{0}'.format(t2 - self.t1)
        file1.writelines('started: ' + t1_str + '\n')
        file1.writelines('duration: ' + d + '\n')
        file1.writelines('------------\n')

    def cmp_entry(self, x=Log_entry, y=Log_entry):
        c = cmp(x.g, y.g)
        if c != 0: return c

        c = cmp(x.l_nb, y.l_nb)
        if c != 0: return c

        c = cmp(x.xy_h[0], y.xy_h[0])
        if c != 0: return c

        return cmp(x.xy_h[1], y.xy_h[1])

    def is_all_done(self, lesson_count=int):
        if len(self.log) < lesson_count: return False
        # -----
        last_run = self.get_max_run_nb()
        if last_run == 0: return False
        # -------
        r = next(filter(lambda x: (x.done == False
                                   or x.run_nb < last_run),
                        self.log.values()), None)
        # ---------
        b = True if r is None else False

        if b:
            b = b

        return b

    def get_max_run_nb(self):
        list_values = [v.run_nb for v in self.log.values()]
        if len(list_values) == 0: return 0
        r = max(list_values)
        return r

    def clear(self):
        self.log.clear()

# l = Lessons()
#
# a = Log()
# a.add(l, True)
# a.add(l, False)
# a.add(l, True)
# a.write()
#
# print(a.is_all_done())
