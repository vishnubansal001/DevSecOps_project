from Model.releaseHistory import CreateReleaseHistory,RetrieveReleaseHistory
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ReleaseHistoryRepository:

    @staticmethod
    async def get_releaseHistorys():
        return await prisma_connection.prisma.releaseHistory.find_many()

    @staticmethod
    async def get_releaseHistory(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.releaseHistory.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(releaseHistory: CreateReleaseHistory):
        if releaseHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.releaseHistory.create({
            "release": releaseHistory.release,
            "created": releaseHistory.created,
            "status": releaseHistory.status,
            "previousStatus": releaseHistory.previousStatus
        })
    
    @staticmethod
    async def update(releaseHistory: RetrieveReleaseHistory):
        if releaseHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.releaseHistory.find_first(where={"identifier": releaseHistory.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.releaseHistory.update({
            where: {"identifier": releaseHistory.identifier},
            data: {
                "release": releaseHistory.release,
                "created": releaseHistory.created,
                "status": releaseHistory.status,
                "previousStatus": releaseHistory.previousStatus
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.releaseHistory.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.releaseHistory.delete(where={"identifier": identifier})