from io import BytesIO
import PIL.Image as Image

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import curve_fit

import sys

sys.path.append(".")
from services.plotter.models import Configurations
from services.plotter.plotter import graph_builder, get_data


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


def run():
    # running from local file
    file_path = "./tests/data/test.csv"
    configurations = Configurations(
        title="This is the title", xlabel="x axis", ylabel="y axis", plot_color="green"
    )

    data = get_data(file_path)
    func1, cov1 = fit_builder(data, "y", Quadratic)
    func2, cov2 = fit_builder(data, "z", Gauss)

    response = graph_builder(file_path, configurations, funcs=[func1, func2])

    image = Image.open(BytesIO(response))
    image.save("services/fitter/tmp/test1.png")


if __name__ == "__main__":
    run()
