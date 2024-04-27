from Model.metalEnvironment import CreateMetalEnvironment,RetrieveMetalEnvironment
from Repository.Database import Database
from fastapi import HTTPException

class MetalEnvironmentService(Database):
    def __init__(self):
        super().__init__()

    async def get_metalEnvironments(self):
        return await self.get_metalEnvironments("metalEnvironment")

    async def get_metalEnvironment(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("metalEnvironment", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, metalEnvironment: CreateMetalEnvironment):
        if metalEnvironment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("metal", metalEnvironment.metal)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("environment", metalEnvironment.environment)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("metalEnvironment", metalEnvironment.dict())

    async def update(self, metalEnvironment: RetrieveMetalEnvironment):
        if metalEnvironment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("metalEnvironment", metalEnvironment.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("metal", metalEnvironment.metal)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("environment", metalEnvironment.environment)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("metalEnvironment", metalEnvironment.identifier, metalEnvironment.dict())
    
    async def delete(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("metalEnvironment", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("metalEnvironment", identifier)