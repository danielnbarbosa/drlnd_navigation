This details the methodology used in evaluating and improving agent learning performance.


#### DQN modifications
Since the original [DQN](https://deepmind.com/research/dqn/) algorithm first came out several enhancements have been proposed.  A couple of those enhancements have been tried here including [Double DQN](https://arxiv.org/abs/1509.06461) and [Dueling networks](https://arxiv.org/abs/1511.06581).

Double DQN leverages both the online network and the target network when calculating q values in an effort to avoid overestimating the q values.
Dueling networks separate estimation of the state value from the state dependent action advantage to better determine state value without having to explore all the associated actions.  Note that in reality dueling networks is a modification of the neural network model and not the algorithm.

All four combinations were tested, each using three different seeds and results are shown below.  The results are the average number of episodes required to solve the environment.  The criteria for solving is considered to be an average score of +13 over 100 consecutive episodes.


|                  | DQN    |  Double DQN |
|------------------|--------|-------------|
| Standard Network | 192.3  | 246.6       |
| Dueling Network  | 247.6  | 290         |


Surprisingly it is clear that vanilla DQN, without any of the enhancements, is the best algorithm for this environment.  This maybe due to the fact that Double DQN and Dueling Networks had the lest impact amongst a variety of enhancments that were brought together in the [Rainbow DQN](https://arxiv.org/abs/1710.02298).


#### Neural network model
As we are dealing with a high dimensional continuous state space, tabular Q learning methods will not be effective here.  Instead we use neural networks to do function approximation and estimate the q values.  The neural network model maps the state (input) to actions (output).  It consists of a two fully connected hidden layers, each with 32 nodes and using relu activation.  Networks with one, two and three hidden layers were all tested and two was found to work best.  In addition the number of nodes in the hidden layer was tried with 16, 32 and 64, and 32 was found to work best.


#### Other hyperparameters
In addition to the DQN algorithm and the neural network model, tweaking epsilon was the other hyperparameter that was found to improve learning speed.  An aggressive epsilon decay rate of 0.97 and a lower bound on epsilon of 0.001 both helped.


#### Learning statistics
See the graphs below for an example of a typical training run.  There are three pairs of graphs for reward, loss and entropy.

- The score (reward) can be seen to be consistently increasing over time.  This is the best indication that the agent is learning.
-  The loss is also increasing over time but this is not typically a problem in reinforcement learning applications as it is not the metric we are trying to minimize.  What are most interested in is converging on a policy that can maximize reward.
- The entropy is decreasing over time.  Entropy is a measure of how certain the agent is of its predictions.  This should decrease over time as the agent learns and gets more confident.

Results vary depending on the seed but typically the agent is able to solve the environment in 150 - 250 episodes.

![results](results.png)


#### Future enhancements
There are plenty more things could be tried to further improve performance, such as:

- Some of the more effective DQN modification cited in Rainbow DQN, like Prioritized Experience Replay and Multi-step Learning.
- A more systematic exploration of the various hyperparameters.
