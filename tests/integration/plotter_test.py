import requests as r
from decouple import config


def test_call_endpoint():
    response = r.get(url=config("PLOTTER_ENDPOINT"))
    assert response.status_code == 200


def test_plot_2d():
    file_path = "./data/test.csv"

    files = {("file", open(file_path, "rb"))}
    payload = {
        "title": "This is a title",
        "xlabel": "x label",
        "ylabel": "y label",
        "grid": True,
        "plot_color": "blue"
    }

    response = r.post(url=config("PLOTTER_ENDPOINT"), files=files, params=payload)
    assert response.status_code == 200
    print(response.content)