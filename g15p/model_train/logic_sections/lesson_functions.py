from g15_new.lessons.lesson_groups import Lsn, Lesson_group, Lesson_groups


def get_lessons_3():
    _lg1_1 = [Lsn(1, 0), Lsn(1, 1), Lsn(1, 2), Lsn(1, 3)]
    _lg1_2 = [Lsn(1, 4), Lsn(1, 5), Lsn(1, 6), Lsn(1, 7)]
    _lg1_3 = [Lsn(1, 8), Lsn(1, 9), Lsn(1, 10), Lsn(1, 11)]
    _lg1_4 = [Lsn(1, 12), Lsn(1, 13), Lsn(1, 14)]

    lg1_1 = Lesson_group(_lg1_1, "lg1_1.txt")
    lg1_2 = Lesson_group(_lg1_2, "lg1_2.txt")
    lg1_3 = Lesson_group(_lg1_3, "lg1_3.txt")
    lg1_4 = Lesson_group(_lg1_4, "lg1_4.txt")

    _lg2_4_lsns = [Lsn(2, 0), Lsn(2, 1), Lsn(2, 2), Lsn(2, 3),
                   Lsn(2, 4), Lsn(2, 5), Lsn(2, 6), Lsn(2, 7)]
    lg2_4_lsns = Lesson_group(_lg2_4_lsns, "lg2___0_3_lsns.txt")

    lg2 = Lesson_group([Lsn(2)], "lg2.txt")
    lg3 = Lesson_group([Lsn(3)], "lg3.txt")
    lg4 = Lesson_group([Lsn(4)], "lg4.txt")
    lg5 = Lesson_group([Lsn(5)], "lg5.txt")
    lg6 = Lesson_group([Lsn(6)], "lg6.txt")
    lg7 = Lesson_group([Lsn(7)], "lg7.txt")
    lg8 = Lesson_group([Lsn(8)], "lg8.txt")
    lg9 = Lesson_group([Lsn(9)], "lg9.txt")
    lg10 = Lesson_group([Lsn(10)], "lg10.txt")
    lg11 = Lesson_group([Lsn(11)], "lg11.txt")
    lg12 = Lesson_group([Lsn(12)], "lg12.txt")
    lg13 = Lesson_group([Lsn(13)], "lg13.txt")
    lg14 = Lesson_group([Lsn(14)], "lg14.txt")
    lg15 = Lesson_group([Lsn(15)], "lg15.txt")

    # return Lesson_groups([lg1_1, lg1_2, lg1_3, lg1_4,
    return Lesson_groups([lg2_4_lsns])


def lsn_15_f(): return Lesson_groups([Lesson_group([Lsn(15)], "lg15.txt")])


def lsn_14_f(): return Lesson_groups([Lesson_group([Lsn(14)], "lg14.txt")])


def lsn_13_f(): return Lesson_groups([Lesson_group([Lsn(13)], "lg13.txt")])


def lsn_10_f(): return Lesson_groups([Lesson_group([Lsn(10)], "lg10.txt")])


def lsn_09_f(): return Lesson_groups([Lesson_group([Lsn(9)], "lg09.txt")])


def lsn_08_f(): return Lesson_groups([Lesson_group([Lsn(8)], "lg08.txt")])


def lsn_07_f(): return Lesson_groups([Lesson_group([Lsn(7)], "lg07.txt")])


def lsn_06_f(): return Lesson_groups([Lesson_group([Lsn(6)], "lg06.txt")])


def lsn_05_f(): return Lesson_groups([Lesson_group([Lsn(5)], "lg05.txt")])


def lsn_04_f(): return Lesson_groups([Lesson_group([Lsn(4)], "lg04.txt")])


def lsn_03_f(): return Lesson_groups([Lesson_group([Lsn(3)], "lg03.txt")])


def lsn_02_f(): return Lesson_groups([Lesson_group([Lsn(2)], "lg02.txt")])


def lsn_01_f(): return Lesson_groups([Lesson_group([Lsn(1)], "lg01.txt")])
