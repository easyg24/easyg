from io import BytesIO

import PIL.Image as Image
import pandas as pd
import matplotlib.pyplot as plt

from models import Configurations


def get_data(file_path):
    df = pd.read_csv(file_path, sep=",", index_col=0)
    return df

def build_configs(configs):
    plt.title(configs.title)
    plt.xlabel(configs.xlabel)
    plt.ylabel(configs.ylabel)
    plt.grid(configs.grid)


def build_plot(data):
    plt.plot(data)
    plt.scatter(data.index, data.y)


def build_graph(data, configs):
    fig = plt.figure()

    build_configs(configs=configs)
    build_plot(data=data)

    buffer = BytesIO()
    fig.savefig(buffer, format="png")

    return buffer.getvalue()

def run():
    # running from local file
    file_path = "../../tests/data/test.csv"
    configurations = Configurations(
        title="This is the title",
        xlabel="x axis",
        ylabel="y axis",
        plot_color="green"
    )

    data = get_data(file_path)
    response = build_graph(data, configurations)

    image = Image.open(BytesIO(response))
    image.save('./tmp/test.png')


if __name__ == "__main__":
    run()