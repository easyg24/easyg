from io import BytesIO

import PIL.Image as Image
import pandas as pd
import matplotlib.pyplot as plt

from services.plotter.models import Configurations


def get_data(file_path):
    df = pd.read_csv(file_path, sep=",", index_col=0)
    return df


def frame_builder(configs):
    plt.title(configs.title)
    plt.xlabel(configs.xlabel)
    plt.ylabel(configs.ylabel)
    plt.grid(configs.grid)


def plot_builder(data, index, funcs):
    # TODO: make it general for all plots
    for i in index:
        plt.plot(data.index, data[i], "o", label=i + " data")

    for i, func in zip(index, funcs):
        plt.plot(data.index, func, label=i + " fit")
    plt.legend()


def graph_builder(file, configs, funcs):
    fig = plt.figure()

    if not configs:
        configs = Configurations()

    if file:
        data = get_data(file)#.file)

    # TODO: validator()
    frame_builder(configs=configs)
    plot_builder(data=data, index=["y", "z"], funcs=funcs)

    buffer = BytesIO()
    fig.savefig(buffer, format="png")

    return buffer.getvalue()
