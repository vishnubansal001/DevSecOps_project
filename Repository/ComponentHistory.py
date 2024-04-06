from Model.componentHistory import CreateComponentHistory,RetrieveComponentHistory
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ComponentHistoryRepository:

    @staticmethod
    async def get_component_histories():
        return await prisma_connection.prisma.componentHistory.find_many()

    @staticmethod
    async def get_component_history(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.componentHistory.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(componentHistory: CreateComponentHistory):
        if componentHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.componentHistory.create({
            "component": componentHistory.component,
            "created": componentHistory.created,
            "operator": componentHistory.operator,
            "previousVersion": componentHistory.previousVersion,
            "previousStatus": componentHistory.previousStatus
        })
    
    @staticmethod
    async def update(componentHistory: RetrieveComponentHistory):
        if componentHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.componentHistory.find_first(where={"identifier": componentHistory.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.componentHistory.update({
            where: {"identifier": componentHistory.identifier},
            data: {
                "component": componentHistory.component,
                "created": componentHistory.created,
                "operator": componentHistory.operator,
                "previousVersion": componentHistory.previousVersion,
                "previousStatus": componentHistory.previousStatus
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.componentHistory.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.componentHistory.delete(where={"identifier": identifier})