from fastapi import FastAPI, HTTPException
import time, random

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/data")
def get_data():
    # Simulate latency
    time.sleep(random.uniform(0.1, 0.5))
    return {"message": "Hello from FastAPI"}

@app.get("/error")
def error():
    raise HTTPException(status_code=500, detail="Simulated error")
