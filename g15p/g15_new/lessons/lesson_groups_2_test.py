from g15_new.lessons.lesson_groups import Lsn, Lesson_group, Lesson_groups
from g15_new.lessons.lessons_v2 import Lessons_v2


def p(l=Lessons_v2):
    print(l.need_walk_around())
    print(l.all_lessons[l.l_indx])
    # print(l.g)
    print(l.g)
    print(l.max_borad_steps())
    for a in l.board(): print(a)
    print("---")


def get_lessons_0():
    # _lg1 = [Lsn(4, 11, (1, 2))]
    # --
    _lg2 = [Lsn(4, 11, (1, 2)),
            Lsn(4, 13, (1, 2))]
    # --
    _lg3 = [Lsn(4, 13, (1, 2)),
            Lsn(4, 11, (1, 2)),
            Lsn(4, 14, (0, 3))]
    # --
    _lg4 = [Lsn(4, 10, (1, 2)),
            Lsn(4, 13, (1, 2)),
            Lsn(4, 11, (1, 2)),
            Lsn(4, 14, (0, 3))]
    # --
    _lg5 = [Lsn(4, 14, (1, 2)),
            Lsn(4, 13, (1, 2)),
            Lsn(4, 10, (1, 2)),
            Lsn(4, 11, (1, 2)),
            Lsn(4, 14, (0, 3))]
    # --
    _lg6 = [Lsn(4, 13, (1, 2)),
            Lsn(4, 11, (1, 2)),
            Lsn(4, 10, (0, 3)),
            Lsn(4, 10, (1, 2)),
            Lsn(4, 14, (1, 2)),
            Lsn(4, 14, (0, 3))]
    # --
    _lg7 = [Lsn(4, 15, (0, 3)),
            Lsn(4, 16, (1, 2)),
            Lsn(4, 13, (1, 2)),
            Lsn(4, 11, (1, 2)),
            Lsn(4, 10, (0, 3)),
            Lsn(4, 10, (1, 2)),
            Lsn(4, 14, (1, 2)),
            Lsn(4, 14, (0, 3))]

    # --
    _lg8 = [Lsn(8)]
    _lg9 = [Lsn(4), Lsn(8)]
    _lg10 = list({Lsn(i) for i in range(1, 16)})

    # lg1 = Lesson_group(_lg1, "lg1.txt")
    lg2 = Lesson_group(_lg2, "lg2.txt")
    lg3 = Lesson_group(_lg3, "lg3.txt")
    lg4 = Lesson_group(_lg4, "lg4.txt")
    lg5 = Lesson_group(_lg5, "lg5.txt")
    lg6 = Lesson_group(_lg6, "lg6.txt")
    lg7 = Lesson_group(_lg7, "lg7.txt")
    lg8 = Lesson_group(_lg8, "lg8.txt")
    lg9 = Lesson_group(_lg9, "lg9.txt")
    lg10 = Lesson_group(_lg10, "lg_all.txt")

    # return Lesson_groups([lg1,
    # return Lesson_groups([lg2,
    #                       lg3, lg4,
    #                       lg5, lg6,
    #                       lg7, lg8,
    #                       lg9, lg10])

    return Lesson_groups([lg2])


def get_lessons_1():
    # (4, 4, (0, 3))
    # (4, 12, (0, 3))
    _lg1 = [Lsn(4, 4, (0, 3)), Lsn(4, 12, (0, 3))]
    # _lg3 = [Lsn(3, 14, (1, 1))]
    # --

    lg1 = Lesson_group(_lg1, "lg4_2_cases.txt")
    # lg2 = Lesson_group(_lg2, "lg4_2_case.txt")
    # lg2 = Lesson_group(_lg2, "lg2.txt")
    # lg3 = Lesson_group(_lg3, "lg3.txt")
    # lg4 = Lesson_group(_lg4, "lg4.txt")
    # lg5 = Lesson_group(_lg5, "lg5.txt")
    # lg6 = Lesson_group(_lg6, "lg6.txt")
    # lg7 = Lesson_group(_lg7, "lg7.txt")
    # lg8 = Lesson_group(_lg8, "lg8.txt")

    return Lesson_groups([lg1])





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
    # return Lesson_groups([lg15])
    # return Lesson_groups([lg2, lg3,
    #                       lg4,
    #                       lg5, lg6, lg7, lg8,
    #                       lg9, lg10, lg13,
    #                       lg14, lg15])
