from Model.componentHistory import CreateComponentHistory,RetrieveComponentHistory
from Repository.Database import Database
from fastapi import HTTPException
from Config.Connection import prisma_connection

class ComponentHistoryService(Database):
    def __init__(self):
        super().__init__()
    
    async def get_componentHistorys():
        return await self.get_all("componenthistory")

    async def get_componentHistory(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.componentHistory.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(componentHistory: CreateComponentHistory):
        return await ComponentHistoryRepository.create(componentHistory)

    async def update(componentHistory: RetrieveComponentHistory):
        return await ComponentHistoryRepository.update(componentHistory)
    
    async def delete(identifier: int):
        return await ComponentHistoryRepository.delete(identifier)