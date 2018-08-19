import time
from collections import deque
import numpy as np
import torch
from plot import plot


def initialize_env(env, brain_name):
    """ Initialize environment and return its initial state. """

    env_info = env.reset(train_mode=True)[brain_name]
    state = env_info.vector_observations[0]
    return state


def env_step(env, brain_name, action):
    """ Given an action, return the state, reward, done. """

    env_info = env.step(action)[brain_name]     # send the action to the environment
    state = env_info.vector_observations[0]     # get the next state
    reward = env_info.rewards[0]                # get the reward
    done = env_info.local_done[0]               # get done status
    return state, reward, done


def train(env, agent, brain_name=None, n_episodes=2000, max_t=1000, eps_start=1.0, eps_end=0.01, eps_decay=0.995, solve_score=10000.0):
    """ Run training loop.

    Params
    ======
        env: Unity Environment object
        agent: Agent object
        brain_name(str): Unity environment brain name
        n_episodes (int): maximum number of training episodes
        max_t (int): maximum number of timesteps per episode
        eps_start (float): starting value of epsilon, for epsilon-greedy action selection
        eps_end (float): minimum value of epsilon
        eps_decay (float): multiplicative factor (per episode) for decreasing epsilon
        solve_score (float): criteria for considering the environment solved
    """
    scores = []                         # list containing scores from each episode
    avg_scores = []                     # list containing average scores after each episode
    scores_window = deque(maxlen=100)   # last 100 scores
    eps = eps_start                     # initialize epsilon
    best_avg_score = -100000            # best score for a single episode
    time_start = time.time()            # track wall time over 100 episodes
    total_steps = 0                     # track steps taken over 100 episodes


    for i_episode in range(1, n_episodes+1):
        state = initialize_env(env, brain_name)
        score = 0
        # loop over steps
        for t in range(max_t):
            # select an action
            action = agent.act(state, eps)
            # take action in environment
            next_state, reward, done = env_step(env, brain_name, action)
            # update agent with returned information
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward
            if done:
                total_steps += t
                break
        eps = max(eps_end, eps_decay*eps)   # decrease epsilon

        # update stats
        scores_window.append(score)         # save most recent score
        scores.append(score)                # save most recent score
        avg_score = np.mean(scores_window)  # average score over window
        avg_scores.append(avg_score)        # save most recent average score
        buffer_len = len(agent.memory)      # number of items in replay buffer
        if avg_score > best_avg_score:      # update best average score
            best_avg_score = avg_score

        # print stats
        print('\rEpisode {:6}\tAvg: {:.2f}\tBest: {:.2f}\tEps: {:.4f}\tBufferLen: {:6}'.format(i_episode, avg_score, best_avg_score, eps, buffer_len), end="")
        if i_episode % 100 == 0:
            # calculate wall time for last 100 episodes
            n_secs = int(time.time() - time_start)
            print('\rEpisode {:6}\tAvg: {:.2f}\tBest: {:.2f}\tEps: {:.4f}\tBufferLen: {:6}\tSteps: {:7}\tSecs: {:4}'.format(i_episode, avg_score, best_avg_score, eps, buffer_len, total_steps, n_secs))
            # reset counters
            time_start = time.time()
            total_steps = 0
        if avg_score >= solve_score:
            print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode-100, avg_score))
            torch.save(agent.qnetwork_local.state_dict(), 'checkpoints/solved.pth')
            break
    plot(scores, avg_scores, agent.loss_list, agent.entropy_list)


def watch(env, agent, brain_name):
    """ Visualize agent using saved checkpoint. """

    # load saved weights
    agent.qnetwork_local.load_state_dict(torch.load('checkpoints/solved.pth'))
    # initialize environment
    state = initialize_env(env, brain_name)
    # interact with environment
    for _ in range(600):
        # slect an action
        action = agent.act(state)
        # add a slight delay otherwise renders too fast to watch
        time.sleep(0.03)
        # take action in environment
        state, _, done = env_step(env, brain_name, action)
        if done:
            break
