import io
import sys

import uvicorn
from decouple import config
from pydantic import Json
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
import PIL.Image as Image

sys.path.append(".")
from services.plotter.plotter import graph_builder
from services.plotter.models import Configurations


app = FastAPI(title="gateway")


@app.post("/", responses={200: {"content": {"image/png": {}}}})
async def plot_request(
    file: Optional[UploadFile] = File(None),
    configs: Optional[Json[Configurations]] = Form(None),
):
    # handle client-side bad requests
    if not file:
        raise HTTPException(status_code=400, detail="File not provided")

    response = graph_builder(file, configs)

    image = Image.open(io.BytesIO(response))
    image.save("services\\plotter\\tmp\\tmp.png")

    return FileResponse("services\\plotter\\tmp\\tmp.png")

@app.get("/")
async def default():
    return {"Hello": "World"}


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    uvicorn.run("server:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run()
