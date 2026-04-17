from fastapi import FastAPI

app = FastAPI(title="Very loaded API")

@app.get("/")
def main():
    return {"message": "Hello from very loaded API"}