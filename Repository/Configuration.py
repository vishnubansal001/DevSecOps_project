from Model.configuration import CreateConfiguration,RetrieveConfiguration
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ConfigurationRepository:

    @staticmethod
    async def get_configurations():
        return await prisma_connection.prisma.configuration.find_many()

    @staticmethod
    async def get_configuration(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.configuration.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(configuration: CreateConfiguration):
        if configuration is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.configuration.create({
            "name": configuration.name,
            "description": configuration.description,
            "status": configuration.status
        })

    @staticmethod
    async def update(configuration: RetrieveConfiguration):
        if configuration is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.configuration.find_first(where={"identifier": configuration.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.configuration.update({
            where: {"identifier": configuration.identifier},
            data: {
                "name": configuration.name,
                "description": configuration.description,
                "status": configuration.status
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.configuration.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.configuration.delete(where={"identifier": identifier})