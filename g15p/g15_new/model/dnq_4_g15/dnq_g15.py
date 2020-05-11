from __future__ import division
from rl.agents import DQNAgent

from g15_new.model.dnq_4_g15.check_points_dict import G15_models_by_goal
from g15_new.g15_env import G15_env


class DQNAgent_g15(DQNAgent):
    def __init__(self,
                 model,
                 env=G15_env,
                 policy=None,
                 test_policy=None,
                 enable_double_dqn=True,
                 enable_dueling_network=False,
                 dueling_type='avg', *args, **kwargs):
        super(DQNAgent_g15, self).__init__(model,
                                           policy,
                                           test_policy,
                                           enable_double_dqn,
                                           enable_dueling_network,
                                           dueling_type,
                                           *args, **kwargs)
        self.env = env
        self.g15_mdls = G15_models_by_goal()
        self.loaded_weights_fp = None

    def forward(self, observation):
        self.load_weights_by_goal()
        return super(DQNAgent_g15, self).forward(observation)

    def load_weights_by_goal(self):
        fp = self.g15_mdls.get_model_weights_filepath(self.env)
        if fp == self.loaded_weights_fp: return
        self.loaded_weights_fp = fp
        self.load_weights(fp)
