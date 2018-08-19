import random
import argparse
from unityagents import UnityEnvironment
from dqn_agent import Agent
from monitor import train, watch

# process command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--render", help="visualize a pre-trained agent", action="store_true")
args = parser.parse_args()

# need to manually set seed to ensure a random environment is initialized
SEED = random.randint(1, 2 ** 30)
# load the environment and default brain
env = UnityEnvironment(file_name="Banana.app", seed=SEED)
brain_name = env.brain_names[0]
# create an agent
agent = Agent(state_size=37, action_size=4, fc1_units=32, fc2_units=32, seed=0)

if args.render:
    watch(env, agent, brain_name=brain_name)
else:
    train(env, agent, brain_name=brain_name, n_episodes=10, eps_start=1.0, eps_end=0.001, eps_decay=0.97, solve_score=13.0)
env.close()
