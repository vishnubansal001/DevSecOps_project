import uvicorn 
from fastapi import FastAPI
from Config.Connection import prisma_connection

def init_app():
    app = FastAPI(
        title="API FastAPI",
        description="API FastAPI",
        version="1.0.0",
    )

    @app.on_event("startup")
    async def startup_event():
        print("Starting up")
        await prisma_connection.connect()

    @app.on_event("shutdown")
    async def shutdown_event():
        print("Shutting down")
        await prisma_connection.disconnect()
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)