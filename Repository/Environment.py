from Model.environment import CreateEnvironment,RetrieveEnvironment
from Config.Connection import prisma_connection
from fastapi import HTTPException

class EnvironmentRepository:

    @staticmethod
    async def get_environments():
        return await prisma_connection.prisma.environment.find_many()

    @staticmethod
    async def get_environment(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.environment.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(environment: CreateEnvironment):
        if environment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.environment.create({
            "fullName": environment.fullName,
            "shortName": environment.shortName,
            "configuration": environment.configuration
        })

    @staticmethod
    async def update(environment: RetrieveEnvironment):
        if environment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.environment.find_first(where={"identifier": environment.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.environment.update({
            where: {"identifier": environment.identifier},
            data: {
                "fullName": environment.fullName,
                "shortName": environment.shortName,
                "configuration": environment.configuration
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.environment.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.environment.delete(where={"identifier": identifier})