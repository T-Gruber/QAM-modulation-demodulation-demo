import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def update_plot():
    ax_left.cla()
    ax_left.plot(x, I*y_cos, "g")
    ax_left.plot(x, -Q*y_sin, "blue")
    ax_left.plot(x, - Q*y_sin + I*y_cos, "r")
    ax_left.legend(["I*cos()", "-Q*sin()", "I*cos()-Q*sin()"])

    ax_right.cla()
    ax_right.arrow(0, 0, I, Q, length_includes_head=True, head_width = 0.1, width = 0.05, ec ='red', fc='red')
    ax_right.grid()
    upper_lim, lower_lim = 1.5, -1.5
    ax_right.set_xlim([lower_lim, upper_lim])
    ax_right.set_ylim([lower_lim, upper_lim])
    ax_right.plot( [upper_lim, lower_lim], [0, 0], "k", linestyle="-")
    ax_right.plot( [0, 0], [upper_lim, lower_lim], "k", linestyle="-")
    ax_right.plot([i[0] for i in symbols], [i[1] for i in symbols], "gray", marker="o", linestyle="", markersize=15)
    ax_right.set_xlabel("I")
    ax_right.set_ylabel("Q")
    for i in range(len(symbols)):
        ax_right.annotate(labels[i], xy=symbols[i], xytext=(symbols[i][0], symbols[i][1]+0.2), horizontalalignment='center', verticalalignment='top', fontsize=20)

    plt.draw()


def submitQ(val):
    global Q
    Q = float(val)
    update_plot()
    

def submitI(val):
    global I
    I = float(val)
    update_plot()



if __name__ == "__main__":

    fig, (ax_left, ax_right) = plt.subplots(1,2)
    plt.subplots_adjust(bottom=0.2)
    fig.suptitle("QAM Modulation", fontsize=24)

    Q, I = 0, 0
    x = np.arange(0.0, 20.0, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    symbols = [(1,1), (-1,1), (-1,-1), (1,-1)]
    labels  = ["00", "01", "11", "10"]

    axboxI = fig.add_axes([0.2, 0.1, 0.2, 0.075])
    text_boxI = Slider(ax=axboxI, label="I", valmin=-1, valmax=1, valinit=0)
    text_boxI.on_changed(submitI)

    axboxQ = fig.add_axes([0.2, 0.05, 0.2, 0.075])
    text_boxQ = Slider(ax=axboxQ, label="Q", valmin=-1, valmax=1, valinit=0)
    text_boxQ.on_changed(submitQ)

    plt.show()


