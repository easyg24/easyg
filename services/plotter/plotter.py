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


def plot_builder(data):
    # here we are just considering one plot labeled y
    # TODO: make it general for all plots
    plt.plot(data)
    plt.scatter(data.index, data.y)


def graph_builder(file, configs):
    fig = plt.figure()

    if not configs:
        configs = Configurations()

    if file:
        data = get_data(file.file)

    # TODO: validator()
    frame_builder(configs=configs)
    plot_builder(data=data)

    buffer = BytesIO()
    fig.savefig(buffer, format="png")

    return buffer.getvalue()
