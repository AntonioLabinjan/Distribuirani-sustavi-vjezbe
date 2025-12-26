from fastapi import FastAPI

app = FastAPI()


@app.post("/login")
def login(username: str):
    return {"token": "very-secure-token"}


@app.get("/verify")
def verify(token: str):
    return {"valid": token == "very-secure-token"}
