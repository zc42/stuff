from g15_new.g15_env import G15_env
from g15_new.hof.hof_1 import get_goal


class G15_models_by_goal():
    def __init__(self, root_dir=None):
        self.dir0 = self.get_dir0(root_dir)
        # self.dir1 = '/check_' + str(nr) + '/'
        self.fname = '/last.hdf5'
        self.m = self.get_dict()

    def get_dir0(self, root_dir):
        if root_dir == None: return './checks/'
        return root_dir + 'checks/'

    def get_dict(self):
        m = dict()

        m[1] = 'lsn_' + self.i2s(1)
        m[2] = 'lsn_' + self.i2s(2)
        m[3] = 'lsn_' + self.i2s(3)
        m[4] = 'lsn_' + self.i2s(4)
        m[5] = 'lsn_' + self.i2s(5)
        m[6] = 'lsn_' + self.i2s(6)
        m[7] = 'lsn_' + self.i2s(7)
        m[8] = 'lsn_' + self.i2s(8)
        m[9] = 'lsn_' + self.i2s(9)
        m[10] = 'lsn_' + self.i2s(10)

        m[13] = 'lsn_' + self.i2s(13)
        m[14] = 'lsn_' + self.i2s(14)

        m[11] = 'lsn_' + self.i2s(15)
        m[12] = 'lsn_' + self.i2s(15)
        m[15] = 'lsn_' + self.i2s(15)

        # kad nebutu error'o kai pabaigia .. goal==0 patampa
        m[0] = 'check_4_base_objctv'

        return m

    def get_model_weights_filepath(self, env=G15_env):
        # b = env.g.ctx.run_base_objective
        # g = 0 if b else env.g.get_goal()
        g = get_goal(env.g.ctx)
        r = self.get_f(g)
        return r

    def get_f(self, g):
        return self.dir0 \
               + self.m[g] \
               + self.fname

    def get_default_check(self):
        return self.get_f(1)

    def i2s(self, i=int):
        r = str(i) if i > 9 else '0' + str(i)
        return r
