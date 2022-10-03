import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.signal import butter, lfilter


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def update_plot():
    order = 6
    fs = 30.0      
    cutoff = 0.3    

    ax_left.cla()
    ax_left.plot(x, I*y_cos, "g")
    ax_left.plot(x, -Q*y_sin, "blue")
    ax_left.plot(x, - Q*y_sin + I*y_cos, "r")
    ax_left.legend(["I*cos()", "-Q*sin()", "I*cos()-Q*sin()"])
    ax_left.set_xlim([0.0, 20.0])

    ax_right.cla()
    ax_right.plot(x, (- Q*y_sin + I*y_cos )* y_cos, "r")
    filtered = butter_lowpass_filter((- Q*y_sin + I*y_cos )* y_cos, cutoff, fs, order)
    ax_right.plot(x, filtered)
    ax_right.plot(x, 2*filtered)
    ax_right.legend(["(I*cos()-Q*sin())*cos()", "I(t)", "2*I(t)"])
    ax_right.set_xlim([0.0, 20.0])
    
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
    fig.suptitle("QAM Demodulation", fontsize=24)

    Q, I = 0, 0
    symbols = [(1,1), (-1,1), (-1,-1), (1,-1)]
    labels  = ["00", "01", "11", "10"]
    x = np.arange(-40.0, 20.0, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    axboxI = fig.add_axes([0.2, 0.1, 0.2, 0.075])
    text_boxI = Slider(ax=axboxI, label="I", valmin=-1, valmax=1, valinit=0)
    text_boxI.on_changed(submitI)

    axboxQ = fig.add_axes([0.2, 0.05, 0.2, 0.075])
    text_boxQ = Slider(ax=axboxQ, label="Q", valmin=-1, valmax=1, valinit=0)
    text_boxQ.on_changed(submitQ)

    plt.show()


