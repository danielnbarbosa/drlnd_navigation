Use [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) to train an agent inside a [Unity-ML](https://github.com/Unity-Technologies/ml-agents) environment.  In particular we will be working in an environment similar to the [Banana Collector](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#banana-collector), however this will be a simplified version using a single agent, a smaller state space and a discrete action space.  This will make it an ideal candidate to leverage a Deep Q Network (DQN).

This project is being done as part of the [Udacity Deep Reinforcement Learning Nanodegree](Environment solved in 327 episodes!	Average Score: 13.06), a four month course that I am enrolled in.  

# Environment Description

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  The goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

- 0 - move forward.
- 1 - move backward.
- 2 - turn left.
- 3 - turn right.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.


# Installation

## Pre-requisites
- [Anaconda](https://www.anaconda.com/download/)


## Clone the repo
Clone this repo using `https://github.com/danielnbarbosa/drlnd_navigation.git`


## Install Dependencies

Assuming you've installed Anaconda you can now create an anaconda environment that contains all the required dependencies to run the project.

Mac:
```
conda create --name rl_unity python=3.6
source activate rl_unity
conda install -y python.app
conda install -y pytorch -c pytorch
pip install torchsummary unityagents
```

Windows:
```
conda create --name rl_unity python=3.6
activate rl_unity
conda install -y pytorch -c pytorch
pip install torchsummary unityagents
```

You will also need to install the pre-built Unity environment, you will NOT need to install Unity itself.  Select the appropriate file for your operating system:

- Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Place the file in the top level directory of the repo and unzip the file.


# Train the agent

To train the agent run `python bananas.py`.  This will fire up the Unity environment and output live training statistics.  When training is finished you'll have a saved model and see some graphs that help visualize the agent's learning progress.  It should take the agent around 150 - 250 episodes to solve the environment.

To watch your trained agent interact with the environment run `python bananas.py --render`.  This will load the saved weights from a checkpoint file.

Mac users will need to use `pythonw` instead of `python` due to matplotlib requiring a framework build of python.  More details [here](https://matplotlib.org/faq/osx_framework.html).
