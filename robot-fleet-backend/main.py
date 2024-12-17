from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Robot Fleet Monitoring Backend is running!"}
