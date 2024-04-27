from Model.request import CreateRequest,RetrieveRequest
from Repository.Database import Database
from fastapi import HTTPException


class RequestService(Database):

    def __init__(self):
        super().__init__()

    async def get_requests(self):
        return await self.get_all("request")

    async def get_request(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("request", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self,request: CreateRequest):
        if request is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("release", request.release)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("request", request.dict())
    
    async def update(self,request: RetrieveRequest):
        if request is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("request", request.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("release", request.release)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("request", request.identifier, request.dict())
    
    async def delete(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("request", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("request", identifier)