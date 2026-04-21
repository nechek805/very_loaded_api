from fastapi import FastAPI

from src.task.router import router as task_router


app = FastAPI(title="Very loaded API")

app.include_router(task_router)

@app.get("/")
def main():
    "This is main fun"
    return {"message": "Hello from very loaded API. You can use it free"}

