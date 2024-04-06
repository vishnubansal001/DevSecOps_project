from Model.metalEnvironment import CreateMetalEnvironment,RetrieveMetalEnvironment
from Config.Connection import prisma_connection
from fastapi import HTTPException

class MetalEnvironmentRepository:

    @staticmethod
    async def get_metalEnvironments():
        return await prisma_connection.prisma.metalEnvironment.find_many()

    @staticmethod
    async def get_metalEnvironment(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.metalEnvironment.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(metalEnvironment: CreateMetalEnvironment):
        if metalEnvironment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.metalEnvironment.create({
            "metal": metalEnvironment.metal,
            "environment": metalEnvironment.environment
        })

    @staticmethod
    async def update(metalEnvironment: RetrieveMetalEnvironment):
        if metalEnvironment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.metalEnvironment.find_first(where={"identifier": metalEnvironment.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.metalEnvironment.update({
            where: {"identifier": metalEnvironment.identifier},
            data: {
                "metal": metalEnvironment.metal,
                "environment": metalEnvironment.environment
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.metalEnvironment.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.metalEnvironment.delete(where={"identifier": identifier})