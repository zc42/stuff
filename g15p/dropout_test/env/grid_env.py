import gym
from gym import spaces
from gym.utils import seeding

from dropout_test.env.grid_4x4 import Game4x4
from dropout_test.env.grid_context import GridCtx


class GridEnv(gym.Env):

    def __init__(self, ctx=GridCtx):
        self.g = Game4x4(ctx)
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(16)

        # self.number = 0
        # self.guess_count = 0
        # self.guess_max = 200
        # self.observation = 0
        # self.reward = 0
        # self.test = ctx.test or ctx.test_rndm
        # self.last_level = 0

        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        act = self.g.ctx.actions[action]
        assert self.action_space.contains(action)
        # self.print_test_info(self.reward)
        self.observation, self.reward, done, a = self.g.make_move(action)
        # self.print_test_info(self.g.ctx, self.reward)
        return self.observation, self.reward, done, {"number": 0}

    # def print_test_info(self, ctx=Ctx, r=int):
    #     if not ctx.render: return
    #     if self.test: prnt_b.pprint_test_info(game=self.g, r=r)

    def reset(self):
        self.g.init()
        self.reward = 0
        self.observation = self.g.state_encoded()
        return self.observation

    def render(self, mode='human'):
        pass

