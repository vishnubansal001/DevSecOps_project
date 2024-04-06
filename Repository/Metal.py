from Model.metal import CreateMetal,RetrieveMetal
from Config.Connection import prisma_connection
from fastapi import HTTPException

class MetalRepository:

    @staticmethod
    async def get_metals():
        return await prisma_connection.prisma.metal.find_many()

    @staticmethod
    async def get_metal(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.metal.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(metal: CreateMetal):
        if metal is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.metal.create({
            "fullName": metal.fullName,
            "shortName": metal.shortName,
            "configuration": metal.configuration
        })
    
    @staticmethod
    async def update(metal: RetrieveMetal):
        if metal is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.metal.find_first(where={"identifier": metal.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.metal.update({
            where: {"identifier": metal.identifier},
            data: {
                "fullName": metal.fullName,
                "shortName": metal.shortName,
                "configuration": metal.configuration
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.metal.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.metal.delete(where={"identifier": identifier})
        