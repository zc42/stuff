from g15_new.g15_env import G15_env


class G15_models_by_goal():
    def __init__(self):
        self.dir = "./checkpoint_test/"
        self.m = self.get_dict()

    def get_dict(self):
        m = dict()
        m[0] = 'weights.lg1.txt__.hdf5'
        m[1] = 'weights.lg1.txt__.hdf5'
        m[2] = 'weights.lg2.txt__.hdf5'
        m[3] = 'weights.lg3.txt__.hdf5'
        m[5] = 'weights.lg5.txt__.hdf5'
        m[6] = 'weights.lg6.txt__.hdf5'
        m[7] = 'weights.lg7.txt__.hdf5'
        m[9] = 'weights.lg9.txt__.hdf5'

        # --------sunkesni---
        m[4] = 'weights.lg4.txt__.hdf5'
        m[8] = 'weights.lg8.txt__.hdf5'
        m[13] = 'weights.lg13.txt__.hdf5'

        # -------uodega-----
        f10='weights.lg10.txt__.hdf5'

        m[10] = 'weights.lg10.txt__.hdf5'
        m[11] = 'weights.lg11.txt__.hdf5'
        m[12] = 'weights.lg12.txt__.hdf5'
        m[14] = 'weights.lg13.txt__.hdf5'
        m[15] = 'weights.lg14.txt__.hdf5'

        m[10] = f10
        m[11] = f10
        m[12] = f10
        m[14] = f10
        m[15] = f10

        return m

    def get_model_weights_filepath(self, env=G15_env):
        g = env.g.get_goal()
        # g_xy = env.g.ctx.init_g_xy
        # h_xy = env.g.ctx.init_h_xy

        # b = g == 4 and h_xy == (0, 3)
        # g = 41 if b and g_xy == (3, 3) else g
        # g = 42 if b and g_xy == (2, 0) else g

        return self.dir + self.m[g]
