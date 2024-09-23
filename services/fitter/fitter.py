from io import BytesIO
import PIL.Image as Image

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import curve_fit

import sys

sys.path.append(".")
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


# Quadratic
def Quadratic(x, A, B):
    y = A * x**2 + B
    return y


def Gauss(x, a, mu, s):
    y = a * np.exp(-((x - mu) ** 2) / (2 * s**2))
    return y


def fit_builder(data, index, function):
    x = np.array(data.index)
    y = np.array(data[index])

    parameters, covariance = curve_fit(function, x, y)

    return function(data.index, *parameters), covariance


def graph_builder(data, configs):
    func1, cov1 = fit_builder(data, "y", Quadratic)
    func2, cov2 = fit_builder(data, "z", Gauss)

    fig = plt.figure()

    # TODO: validator()
    frame_builder(configs=configs)
    plot_builder(data=data, index=["y", "z"], funcs=[func1, func2])

    plt.show()

    buffer = BytesIO()
    fig.savefig(buffer, format="png")

    return buffer.getvalue()


def run():
    # running from local file
    file_path = "./tests/data/test.csv"
    configurations = Configurations(
        title="This is the title", xlabel="x axis", ylabel="y axis", plot_color="green"
    )

    data = get_data(file_path)
    response = graph_builder(data, configurations)

    image = Image.open(BytesIO(response))
    image.save("services/fitter/tmp/test.png")


if __name__ == "__main__":
    run()
