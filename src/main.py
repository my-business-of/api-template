from fastapi import FastAPI

app = FastAPI()


@app.get("/server_status")
def server_status():
    return {"status": "All great, all nice!"}
