import numpy as np
import matplotlib.pyplot as plt

def sub_plot(coords, data, y_label='', x_label=''):
    """ Plot a single graph (subplot). """

    plt.subplot(coords)
    plt.plot(np.arange(len(data)), data)
    plt.ylabel(y_label)
    plt.xlabel(x_label)


def plot(scores, avg_scores, loss_list, entropy_list):
    """ Plot all data from training run. """

    window_size = len(loss_list) // 100 # window size is 1% of total steps
    plt.figure(1)
    # plot score
    sub_plot(231, scores, y_label='Score')
    sub_plot(234, avg_scores, y_label='Avg Score', x_label='Episodes')
    # plot loss
    sub_plot(232, loss_list, y_label='Loss')
    avg_loss = np.convolve(loss_list, np.ones((window_size,))/window_size, mode='valid')
    sub_plot(235, avg_loss, y_label='Avg Loss', x_label='Steps')
    # plot entropy
    sub_plot(233, entropy_list, y_label='Entropy')
    avg_entropy = np.convolve(entropy_list, np.ones((window_size,))/window_size, mode='valid')
    sub_plot(236, avg_entropy, y_label='Avg Entropy', x_label='Steps')

    plt.show()
