import uvicorn 
from fastapi import FastAPI

def init_app():
    app = FastAPI(
        title="API FastAPI",
        description="API FastAPI",
        version="1.0.0",
    )
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)