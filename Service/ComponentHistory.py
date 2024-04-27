from Model.componentHistory import CreateComponentHistory,RetrieveComponentHistory
from Repository.Database import Database
from fastapi import HTTPException
from Config.Connection import prisma_connection

class ComponentHistoryService(Database):
    def __init__(self):
        super().__init__()
    
    async def get_componentHistorys(self):
        return await self.get_all("componenthistory")

    async def get_componentHistory(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("componenthistory", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, componentHistory: CreateComponentHistory):
        if componentHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("component", componentHistory.component)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await self.get_one("operator", componentHistory.operator)
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("componenthistory", componentHistory.dict())

    async def update(self, componentHistory: RetrieveComponentHistory):
        if componentHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("componenthistory", componentHistory.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await self.get_one("component", componentHistory.component)
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        t = await self.get_one("operator", componentHistory.operator)
        if t is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("componenthistory", componentHistory.identifier, componentHistory.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("componenthistory", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("componenthistory", identifier)