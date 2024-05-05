from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}

@app.get("/hello")
def read_hello():
    return {"message": "Hello, World"}
