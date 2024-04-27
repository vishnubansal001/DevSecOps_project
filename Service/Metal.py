from Model.metal import CreateMetal,RetrieveMetal
from Repository.Database import Database
from fastapi import HTTPException

class MetalService(Database):
    def __init__(self):
        super().__init__()

    async def get_metals(self):
        return await self.get_all("metal")

    async def get_metal(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("metal", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, metal: CreateMetal):
        if metal is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("configuration", metal.configuration)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await self.get_one("configuration", metal.configuration)
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("metal", metal.dict())

    async def update(self, metal: RetrieveMetal):
        if metal is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("metal", metal.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await self.get_one("configuration", metal.configuration)
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("metal", metal.identifier, metal.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("metal", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("metal", identifier)