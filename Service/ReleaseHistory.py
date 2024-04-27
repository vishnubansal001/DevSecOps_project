from Model.releaseHistory import CreateReleaseHistory,RetrieveReleaseHistory
from Repository.Database import Database
from fastapi import HTTPException


class ReleaseHistoryService(Database):
    def __init__(self):
        super().__init__()

    async def get_releaseHistorys(self):
        return await self.get_all("releaseHistory")

    async def get_releaseHistory(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("releaseHistory", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self,releaseHistory: CreateReleaseHistory):
        if releaseHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("release", releaseHistory.release)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("releaseHistory", releaseHistory.dict())

    async def update(self,releaseHistory: RetrieveReleaseHistory):
        if releaseHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("releaseHistory", releaseHistory.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("release", releaseHistory.release)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("releaseHistory", releaseHistory.identifier, releaseHistory.dict())
    
    async def delete(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("releaseHistory", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("releaseHistory", identifier)