import uvicorn
from decouple import config
from fastapi import FastAPI, File, UploadFile


app = FastAPI(title="api")


@app.post("/")
async def plot_request(upload_file: UploadFile = File(...)):
    return {"file": "File received"}


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    uvicorn.run("server:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run()
