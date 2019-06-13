from env import ArmEnv
from rl import DDPG
import matplotlib.pyplot as plt
import time

MAX_EPISODES = 4000
MAX_EP_STEPS = 200
ON_TRAIN = False

# set env
env = ArmEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# set RL method (continuous)
rl = DDPG(a_dim, s_dim, a_bound)

steps = []
def train():
    # start training
    for i in range(MAX_EPISODES):
        s = env.reset()
        ep_r = 0.
        for j in range(MAX_EP_STEPS):
            # env.render()

            a = rl.choose_action(s)

            s_, r, done = env.step(a)


            rl.store_transition(s, a, r, s_)

            ep_r += r
            if rl.memory_full:
                # start to learn once has fulfilled the memory
                rl.learn()

            s = s_
            if done or j == MAX_EP_STEPS-1:
                print('Ep: %i | %s | ep_r: %.1f | step: %i' % (i, '---' if not done else 'done', ep_r, j))
                steps.append(j)
                break
        if i%100 == 0:
            rl.save()


def eval():
    rl.restore()
    env.render()
    env.viewer.set_vsync(True)
    s = env.reset()
    while True:
        env.render()
        a = rl.choose_action(s)
        s, r, done = env.step(a)



if __name__ == '__main__':

    if ON_TRAIN:
        train()
        plt.figure()
        plt.plot(range(MAX_EPISODES), steps , '-b')
        current_time = time.time()
        plt.savefig("./result/step_"+str(current_time)+".png")
        plt.show()
        eval()
    else:
        eval()
