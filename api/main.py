from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "hello world"}


@app.post('/name/')
async def remind_name(name : Name):
    return name