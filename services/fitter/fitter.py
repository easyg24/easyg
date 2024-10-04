import numpy as np
from scipy.optimize import curve_fit

import sys

sys.path.append(".")
from services.plotter.models import Configurations
from services.plotter.plotter import graph_builder_plotter, get_data


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


def graph_builder_fitter(file, configs, funcs):
    if not configs:
        configs = Configurations()

    if file:
        data = get_data(file.file)

    func1, cov1 = fit_builder(data, "y", Quadratic)
    func2, cov2 = fit_builder(data, "z", Gauss)

    return graph_builder_plotter(data, configs, funcs=[func1, func2])
