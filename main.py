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

    from Controller import Product, Configuration, Metal, Operator, Role, Request, Release, Component, Environment, ComponentHistory, ReleaseHistory, ProductHistory, ProductComponent, OperatorRole, MetalEnvironment
    app.include_router(Product.router)
    app.include_router(Configuration.router)
    app.include_router(Metal.router)
    app.include_router(Operator.router)
    app.include_router(Role.router)
    app.include_router(Request.router)
    app.include_router(Release.router)
    app.include_router(Component.router)
    app.include_router(Environment.router)
    app.include_router(ComponentHistory.router)
    app.include_router(ReleaseHistory.router)
    app.include_router(ProductHistory.router)
    app.include_router(ProductComponent.router)
    app.include_router(OperatorRole.router)
    app.include_router(MetalEnvironment.router)
    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)