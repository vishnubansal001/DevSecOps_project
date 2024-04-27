from Model.environment import CreateEnvironment,RetrieveEnvironment
from Repository.Database import Database
from fastapi import HTTPException

class EnvironmentService(Database):
    def __init__(self):
        super().__init__()

    async def get_environments(self):
        return await self.get_all("environment")

    async def get_environment(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("environment", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, environment: CreateEnvironment):
        if environment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("configuration", environment.configuration)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("environment", environment.dict())

    async def update(self, environment: RetrieveEnvironment):
        if environment is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("environment", environment.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await self.get_one("configuration", environment.configuration)
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("environment", environment.identifier, environment.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("environment", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("environment", identifier)