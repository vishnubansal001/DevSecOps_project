from Model.configuration import CreateConfiguration,RetrieveConfiguration
from Repository.Database import Database
from fastapi import HTTPException

class ConfigurationService(Database):
    def __init__(self):
        super().__init__()

    async def get_configurations(self):
        return await self.get_all("configuration")

    async def get_configuration(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("configuration", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, configuration: CreateConfiguration):
        if configuration is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("configuration", configuration.dict())

    async def update(self, configuration: RetrieveConfiguration):
        if configuration is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("configuration", configuration.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("configuration", configuration.identifier, configuration.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("configuration", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("configuration", identifier)