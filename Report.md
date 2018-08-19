Since the original [DQN](https://deepmind.com/research/dqn/) algorithm first came out several enhancements have been proposed.  A couple of those enhancements have been tried here including [Double DQN](https://arxiv.org/abs/1509.06461) and [Dueling networks](https://arxiv.org/abs/1511.06581).  Double DQN leverages both the online network and the target network when calculating q values in an effort to avoid overestimating the q values.  Dueling networks separate estimation of the state value from the state dependent action advantage to better determine state value without having to explore all the associated actions.  All four combinations were tested, each using three different seeds and results are shown below.  The results are the average number of episodes required to solve the environment.  The criteria for solving is considered to be an average score of +13 over 100 consecutive episodes.


|                  | DQN    |  Double DQN |
|------------------|--------|-------------|
| Standard Network | 192.3  | 246.6       |
| Dueling Network  | 247.6  | 290         |


From this it is clear that vanilla DQN is the best algorithm for this environment.

The neural network model maps the state (input) to actions (output).  It consists of a two fully connected hidden layers, each with 32 nodes and using relu activation.  Networks with one, two and three hidden layers were all tested and two was found to work best.  In addition the number of nodes in the hidden layer was tried with 16, 32 and 64, and 32 was found to work best.


In addition to the DQN algorithm and the neural network model, tweaking epsilon was the other hyperparameter that was found to improve learning speed.  An aggressive epsilon decay rate of 0.97 and a lower bound on epsilon of 0.001 both helped.

See the ![results](results.png) for graphs of a typical training run.  There are three pairs of graphs  The first show the score (reward) improving over time.  The second shows the loss also increases over time but this is not typically a problem in reinforcement learning applications as it is not the metric we are trying to minimize.  What are most interested in is converging in a policy that can maximize reward.  The third shows the entropy decreasing over time.  Entropy is a measure of how certain the agent is of its predictions.  This should decrease over time as the agent learns and gets more confident in its predictions.

Typically the agent is able to solve the environment in 150 - 250 episodes.
