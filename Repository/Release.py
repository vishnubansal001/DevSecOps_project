from Model.release import CreateRelease,RetrieveRelease
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ReleaseRepository:

    @staticmethod
    async def get_releases():
        return await prisma_connection.prisma.release.find_many()

    @staticmethod
    async def get_release(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.release.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(release: CreateRelease):
        if release is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.metalenvironment.find_first(where={"identifier": release.metalEnvironment})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.release.create({
            "scope": release.scope,
            "status": release.status,
            "effect": release.effect,
            "metalEnvironment": release.metalEnvironment
        })
    
    @staticmethod
    async def update(release: RetrieveRelease):
        if release is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.release.find_first(where={"identifier": release.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.metalenvironment.find_first(where={"identifier": release.metalEnvironment})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.release.update({
            where: {"identifier": release.identifier},
            data: {
                "scope": release.scope,
                "status": release.status,
                "effect": release.effect,
                "metalEnvironment": release.metalEnvironment
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.release.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.release.delete(where={"identifier": identifier})