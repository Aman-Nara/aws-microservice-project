from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Containerized microservice running on AWS!"}

@app.get("/info")
def get_info():
    return {"service": "assessment-api", "version": "1.0.0"}