from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get('/')
def health_check():
    return "Ok, it's working"

app.include_router(router)
