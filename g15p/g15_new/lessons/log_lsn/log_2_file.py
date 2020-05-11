from g15_new.g15_context import Ctx


def log_lsn_progress(ctx=Ctx, r=int, f=bool):
    if ctx.keyboard: return
    if ctx.run_base_objective: return
    ctx.lesns_log_name = ctx.lessons.get_log_name()
    add_log1(ctx, r, f)
    ctx.save_chk_point = False

    lsn_nb = len(ctx.lessons.all_lessons)
    if ctx.log.is_all_done(lsn_nb): next_lsn_grp(ctx)

    # if ctx.lessons.group_lessons_done(): next_lsn_grp(ctx)
    if ctx.lessons.all_groups_done():
        ctx.done = True


def add_log1(ctx=Ctx, r=int, f=bool):
    if f == False: return
    fail = r < 1
    ctx.lessons.current_lesson_done(not fail)
    ctx.log.add(ctx.lessons, fail)
    if not need_write2file(ctx): return

    if ctx.runs_count % ctx.log_write_count == 0: ctx.log.write()


def next_lsn_grp(ctx=Ctx):
    ctx.save_chk_point = True
    if need_write2file(ctx): ctx.log.write()
    ctx.lessons.group_lessons_done()
    ctx.lessons.next_lsn_grp()
    ctx.log.clear()


def need_write2file(ctx):
    b = not ctx.test
    b = b and not ctx.test_rndm
    b = b and not ctx.keyboard
    return b
