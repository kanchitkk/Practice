from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return '123 Hello World - 12345678910!'