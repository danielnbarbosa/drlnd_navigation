This documents detailed results on the number of episodes it took to solve the environment using a variety of different hyperparameters.


## DQN Modifications
Hidden layers kept fixed at fc1_units=32, fc2_units=32

#### Standard DQN
- Environment solved in 254 episodes!	Average Score: 13.14
- Environment solved in 157 episodes!	Average Score: 13.00
- Environment solved in 166 episodes!	Average Score: 13.06
- Avg: 192.3


#### Double DQN
- Environment solved in 222 episodes!	Average Score: 13.02
- Environment solved in 281 episodes!	Average Score: 13.03
- Environment solved in 237 episodes!	Average Score: 13.02
- Avg: 246.6


#### Dueling DQN
- Environment solved in 219 episodes!	Average Score: 13.03
- Environment solved in 262 episodes!	Average Score: 13.10
- Environment solved in 262 episodes!	Average Score: 13.02
- Avg: 247.6


#### Double Dueling DQN
- Environment solved in 248 episodes!	Average Score: 13.12
- Environment solved in 295 episodes!	Average Score: 13.06
- Environment solved in 327 episodes!	Average Score: 13.06
- Avg: 290


## Model layer size modifications (fc1_units, fc2_units)
Using Standard DQN

#### (16, 16)
- Environment solved in 226 episodes!	Average Score: 13.04
- Environment solved in 182 episodes!	Average Score: 13.01
- Environment solved in 205 episodes!	Average Score: 13.04
- Avg: 204.33

#### (32, 32)
- Environment solved in 254 episodes!	Average Score: 13.14
- Environment solved in 157 episodes!	Average Score: 13.00
- Environment solved in 166 episodes!	Average Score: 13.06
- Avg: 192.3

#### (64, 64)
- Environment solved in 238 episodes!	Average Score: 13.09
- Environment solved in 206 episodes!	Average Score: 13.04
- Environment solved in 302 episodes!	Average Score: 13.08
- Avg: 248.6

#### (32, 16)
- Environment solved in 397 episodes!	Average Score: 13.01
- Environment solved in 281 episodes!	Average Score: 13.07
- Environment solved in 223 episodes!	Average Score: 13.04
- Avg: 300.3

#### (64, 32)
- Environment solved in 188 episodes!	Average Score: 13.05
- Environment solved in 217 episodes!	Average Score: 13.03
- Environment solved in 190 episodes!	Average Score: 13.06
- Avg: 198.3
