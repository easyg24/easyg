import os
import pytest

from fastapi.testclient import TestClient
from server import app


client = TestClient(app)


def test_gateway_upload_file():
    file_path = "../tests/data/test.csv"

    if os.path.isfile(file_path):
        file = {"upload_file": ("test.csv", open(file_path, "rb"))}
        response = client.post("/", files=file)
        assert response.status_code == 200
        assert response.json() == {"file": "File received"}
    else:
        pytest.fail("Scratch file does not exists.")
